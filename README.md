# N - Queens Visualizer

This project visualizes the solution of the N-Queens problem using PyQt5 for the user interface and Pygame for the graphical representation. The N-Queens problem involves placing N queens on an N×N chessboard so that no two queens threaten each other. Thus, a queen can attack another queen if they are in the same row, column, or diagonal.

## Features

- **Interactive Input**: Users can input the number of queens and choose the visualization speed.
- **Visualization**: Provides a visual representation of how the algorithm places queens on the chessboard.
- **All Solutions**: Option to visualize all possible solutions to the N-Queens problem.

## Technologies Used

- **PyQt5**: Used for creating the interactive input window.
- **Pygame**: Used for rendering the chessboard and queen images, as well as handling the graphical representation of the algorithm.

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/n-queens-visualizer.git
   cd n-queens-visualizer
   ```

2. **Create a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## How to Use

1. **Run the application**:

   ```bash
   python src/main.py
   ```

2. **Input Window**:
   - Enter the number of queens in the text field.
   - Select the visualization speed using the slider.
   - Click "Start" to begin the visualization.

## Visualization

Upon clicking "Start," the program will display the N-Queens solution process:

- Queens will be placed on the chessboard, and the program will highlight conflicts.
- The visualization will show all possible solutions for the given input one by one.

## Assets

- Place the `queen.png` image in the `assets/` directory for the queen representation.

## Contributing

Feel free to submit issues or pull requests. Contributions are welcome!

## Demo

You can view a demo of the application [here](https://github.com/user-attachments/assets/0b84ecc7-1cac-4d27-9c99-6366f65f0b4f)
