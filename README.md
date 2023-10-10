<p align="center">
 <img width="200px" src="https://github.com/HenokB/file-converter/assets/46082799/fa1459e2-0213-4f1a-ab85-8313719d82ec" align="center" alt="file_converter" />
 <h2 align="center">file_converter</h2>
 <p align="center">A simple and efficient file converter package for various data file types. </p>
</p>
</p>
  <p align="center">
    <a href="https://github.com/HenokB/file-converter/graphs/contributors">
      <img alt="GitHub Contributors" src="https://img.shields.io/github/contributors/HenokB/file-converter" />
    </a>
    <a href="https://codecov.io/gh/HenokB/file-converter">
      <img alt="Tests Coverage" src="https://codecov.io/gh/HenokB/file-converter/branch/master/graph/badge.svg" />
    </a>
    <a href="https://github.com/HenokB/file-converter/issues">
      <img alt="Issues" src="https://img.shields.io/github/issues/HenokB/file-converter?color=0088ff" />
    </a>
    <a href="https://github.com/HenokB/file-converter/pulls">
      <img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/HenokB/file-converter?color=0088ff" />
    </a>
    <br />
    <br />
    <a href="https://a.paddle.com/v2/click/16413/119403?link=1227">
      <img src="https://img.shields.io/badge/Supported%20by-VSCode%20Power%20User%20%E2%86%92-gray.svg?colorA=655BE1&colorB=4F44D6&style=for-the-badge"/>
    </a>
    </a>
  </p>

### Features

- Convert CSV to JSON and vice versa.
- Convert CSV to TXT and vice versa.
- Convert JSON to TXT and vice versa.
- (More conversion features to be added…)

### Installation

```bash
pip install file_converter
```

<h3>Usage:</h3>
<pre>
import file_converter

## Example usage:
### Convert JSON to CSV
```bash
file_converter.FileConverter.json_to_csv("input_file.json", "output_file.csv")
```
### Convert CSV to TXT

```bash
file_converter.FileConverter.csv_to_txt("input_file.csv", "output_file.txt")
```

### Convert CSV to JSON
```bash
file_converter.FileConverter.csv_to_json("input_file.csv", "output_file.json")
```
### Convert TXT to CSV

```bash
file_converter.FileConverter.txt_to_csv("input_file.txt", "output_file.csv")
```
</pre>

<!-- <h3>Parameters:</h3>
<p>Each method has specific parameters which can be found in the docstrings of the method implementations.</p>

<h3>Installation:</h3>
<p>Provide instructions on how to install your library, perhaps using pip or by cloning the repository.</p>

<h3>Contributing:</h3>
<p>Instructions for how others can contribute to your project.</p>

<h3>License:</h3>
<p>Specify the license under which your project is available.</p> -->
