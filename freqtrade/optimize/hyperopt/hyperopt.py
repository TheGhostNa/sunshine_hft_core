import os
import optuna
import rapidjson
import logging
import multiprocessing
from typing import Any, Dict, Tuple
from datetime import datetime
from freqtrade.optimize.backtesting import backtest_one_strategy
from freqtrade.optimize.hyperopt import (
    load_hyperopt_class,
    load_parameter_file,
    get_optimization_space
)
from freqtrade.configuration import Configuration
from freqtrade.optimize.logging_opt import logging_mp_setup

log_queue: Any = None  # Global log queue for multiprocessing

def _objective_wrapper(study: optuna.Study, trial: optuna.Trial) -> float:
    config = Configuration()
    hopt = load_hyperopt_class(config)
    parameters = get_optimization_space(hopt, trial)

    results = backtest_one_strategy(config=config, strategy_parameters=parameters)
    return -results[0]['profit_total_abs']

def _worker(
    study_name: str,
    storage_url: str,
    direction: str,
    timeout: int
) -> None:
    global log_queue
    log_queue = multiprocessing.Queue()
    logging_mp_setup(log_queue)

    study = optuna.load_study(study_name=study_name, storage=storage_url, direction=direction)
    study.optimize(_objective_wrapper, timeout=timeout)

def run_optimization(
    config_path: str,
    strategy_name: str,
    max_trials: int = 100,
    timeout: int = 1800,
    n_jobs: int = 1
) -> Tuple[optuna.Study, Dict[str, Any]]:
    config = Configuration.from_files([config_path])
    config['strategy'] = strategy_name
    hopt = load_hyperopt_class(config)

    study = optuna.create_study(direction="maximize")
    print(f"Starting optimization with strategy: {strategy_name}")

    if n_jobs > 1:
        processes = []
        for _ in range(n_jobs):
            p = multiprocessing.Process(
                target=_worker,
                args=(study.study_name, study._storage._url, "maximize", timeout)
            )
            p.start()
            processes.append(p)
        for p in processes:
            p.join()
    else:
        study.optimize(lambda trial: -_objective_wrapper(study, trial), n_trials=max_trials, timeout=timeout)

    best_params = study.best_params
    best_value = study.best_value

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    result_file = f"hyperopt_result_{strategy_name}_{timestamp}.json"
    result_path = os.path.join("hyperopt_results", result_file)

    os.makedirs("hyperopt_results", exist_ok=True)
    with open(result_path, "w") as f:
        rapidjson.dump({
            "best_params": best_params,
            "best_value": best_value
        }, f, indent=4)

    print(f"Optimization complete. Results saved to: {result_path}")
    return study, best_params

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Run Optuna Hyperopt.")
    parser.add_argument("--config", required=True, help="Path to config.json")
    parser.add_argument("--strategy", required=True, help="Strategy name")
    parser.add_argument("--trials", type=int, default=100, help="Max number of trials")
    parser.add_argument("--timeout", type=int, default=1800, help="Max time in seconds")
    parser.add_argument("--jobs", type=int, default=1, help="Number of parallel jobs")

    args = parser.parse_args()

    run_optimization(
        config_path=args.config,
        strategy_name=args.strategy,
        max_trials=args.trials,
        timeout=args.timeout,
        n_jobs=args.jobs
    )
