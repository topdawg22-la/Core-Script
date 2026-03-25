# Contributing to Nexus-Auto-OS
**Lead Architect:** Gunner Blake Carr, B.S. Systems Engineering & Software Development (CTU)

Thank you for your interest in scaling the future of automotive diagnostics. To maintain the integrity of this framework, all contributors must adhere to the following engineering standards.

## 🛠 Engineering Standards
1. **Safety First:** Any code affecting bi-directional ECU control must include fail-safes to prevent "bricking" a module.
2. **Documentation:** Every function must be documented. We are building a professional product, not a script.
3. **Testing:** All Pull Requests must be verified against a physical CAN-bus interface or a simulated Docker environment.

## 🤝 The "Profit-Share" Protocol
Contributions that add support for new manufacturers (Tesla, Ford, Apple Car-Integrations) will be prioritized. By contributing, you agree to the **GNU GPLv3 License**, ensuring this remains an open and profitable ecosystem for all.

## 🚀 Pull Request Process
- Open an Issue first to discuss the feature.
- Follow the `GITMORE` template for all descriptions.
- Ensure your code passes the Python `flake8` linting standards.
