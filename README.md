# Flight-Probability-Analyzer

This project analyzes flight data to determine the probability of having at least 6 flights of more than 700 km per month. The data is loaded from a JSON file and processed using the Python programming language.

## Requirements

To run this project, you will need:

- Python 3
- The following Python packages:
  - json
  - collections
  - datetime
  - scipy

## Usage

1. Clone this repository to your local machine.
2. Navigate to the project directory in your terminal.
3. Run the following command: `python main.py`
4. The program will output the probability of having at least 6 flights of more than 700 km per month for each month of the year.

## Data

The flight data is stored in the `data.json` file. It contains the following fields for each flight:

- `date` (string): The date of the flight in the format "DD.MM.YYYY".
- `km` (integer): The distance of the flight in kilometers.

## Contributing

If you would like to contribute to this project, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
