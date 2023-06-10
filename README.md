# tiafork: Toolkit for Integration and Analysis (Fork of a Fork)

## This is a Fork of a Fork!
This project is a fork of the Python 3 compliant version of the `tia` toolkit made by [PaulMest](https://github.com/PaulMest/tia). We've named it `tiafork`.

The original `tia` project was developed with Python 2. PaulMest updated it to be Python 3 compliant, and this project, `tiafork`, builds upon that work. This version is also Python 3 compliant and **NOT** Python 2 compliant.

We are open to additional community contributions. Just submit a pull request.

## Overview
TIAFORK is a toolkit that provides Bloomberg data access, easier PDF generation, backtesting functionality, technical analysis functionality, return analysis, and a few windows utils.

## Examples

Bloomberg API
- [v3 api](http://nbviewer.ipython.org/github/yourusername/tiafork/blob/master/examples/v3api.ipynb)
- [Data Manager](http://nbviewer.ipython.org/github/yourusername/tiafork/blob/master/examples/datamgr.ipynb)

Simple Trade and Portfolio Model
- [model](http://nbviewer.ipython.org/github/yourusername/tiafork/blob/master/examples/model_usage.ipynb)

PDF Generation (using reportlab)
- [pdf generation](http://nbviewer.ipython.org/github/yourusername/tiafork/blob/master/examples/rlab_usage.ipynb)
- [dataframe to pdf table](http://nbviewer.ipython.org/github/yourusername/tiafork/blob/master/examples/rlab_table_example.ipynb)
- [quick styling of pdf tables](http://nbviewer.ipython.org/github/yourusername/tiafork/blob/master/examples/rlab_table_style.ipynb)

Technical Analysis
- [pure python and ta-lib](http://nbviewer.ipython.org/github/yourusername/tiafork/blob/master/examples/ta.ipynb)

Backtest
- [backtest with yahoo data](http://nbviewer.ipython.org/github/yourusername/tiafork/blob/master/examples/backtest.ipynb)
- backtest with bbg data and pdf (Soon)

Utils
- [Formatting](http://nbviewer.ipython.org/github/yourusername/tiafork/blob/master/examples/fmt.ipynb)

## Dependencies
- Python 3

### Mandatory
- [numpy](http://www.numpy.org/)
- [pandas](http://pandas.pydata.org/)

### Recommended
- [matplotlib](http://matplotlib.sourceforge.net)

### Optional
- [reportlab](http://www.reportlab.com/)
- [ta-lib](http://mrjbq7.github.io/ta-lib/)
- [bloomberg](http://www.bloomberglabs.com/api/libraries/)

## Installation
To install `tiafork`, simply:

    $ pip install tiafork
