use std::collections::HashMap;

#[derive(Debug)]
pub struct RiskModel {
    risk_limits: HashMap<String, f64>,
}

impl RiskModel {
    pub fn new() -> Self {
        RiskModel {
            risk_limits: HashMap::new(),
        }
    }

    pub fn set_limit(&mut self, strategy: &str, limit: f64) {
        self.risk_limits.insert(strategy.to_string(), limit);
    }

    pub fn evaluate(&self, strategy: &str, risk_score: f64) -> bool {
        match self.risk_limits.get(strategy) {
            Some(&limit) => risk_score <= limit,
            None => true, // allow if no limit set
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_risk_model_limits() {
        let mut model = RiskModel::new();
        model.set_limit("MACD", 0.7);
        assert!(model.evaluate("MACD", 0.6));
        assert!(!model.evaluate("MACD", 0.9));
        assert!(model.evaluate("RSI", 0.5)); // no limit set
    }
}
