# DICOM File Anonymizer in Python

This project is a tool to **anonymize DICOM files** using Python. It is designed to remove or modify personally identifiable information (PII) in DICOM files, facilitating compliance with privacy regulations in medical data handling.

## Features
- Removes specific DICOM tags containing sensitive information.
- Modifies or deletes names, IDs, and other personal data in DICOM files.
- Supports batch processing for multiple files.
- Easy to use and configure.

## Installation

### Prerequisites
This project requires Python 3.6 or higher. Make sure you have `pip` installed to manage dependencies.

### Dependencies
Install the required libraries using the `requirements.txt` file or manually with pip:

```bash
pip install pydicom
