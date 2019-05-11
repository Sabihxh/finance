<p align="center"><img width="40%" src="doc/static/allennlp-logo-dark.png" /></p>

[![Build Status](http://build.allennlp.org/app/rest/builds/buildType:(id:AllenNLP_AllenNLPCommits)/statusIcon)](http://build.allennlp.org/viewType.html?buildTypeId=AllenNLP_AllenNLPCommits&guest=1)
[![codecov](https://codecov.io/gh/allenai/allennlp/branch/master/graph/badge.svg)](https://codecov.io/gh/allenai/allennlp)

An [Apache 2.0](https://github.com/allenai/allennlp/blob/master/LICENSE) NLP research library, built on PyTorch,
for developing state-of-the-art deep learning models on a wide variety of linguistic tasks.

## Quick Links

* [Website](http://www.allennlp.org/)
* [Tutorial](https://allennlp.org/tutorials)
* [Documentation](https://allenai.github.io/allennlp-docs/)
* [Contributing Guidelines](CONTRIBUTING.md)
* [Model List](MODELS.md)
* [Continuous Build](http://build.allennlp.org/)



## Trading Strategies

This project aims to implement trading strategies and test them on FTSE 350 stocks. 

The jupyter notebook **strategies.ipynb** contains the mock up of trading strategies. 

The data_stocks directory contains data for all FTSE 350 companies starting from 2014-01-01.

**To do:**
- Move trading strategies from notebook to .py module
- Get data going back as early as possible for all stocks instead of 2014-01-01
- Write tests
- Implement more strategies
- Use google storage for data



