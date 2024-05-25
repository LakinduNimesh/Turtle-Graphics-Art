
# Turtle Graphics Art

This project creates an intricate and colorful pattern using the Turtle graphics module in Python. The code utilizes loops and Turtle's drawing capabilities to produce an eye-catching design.

![image](https://github.com/LakinduNimesh/Turtle-Graphics-Art/assets/149768006/4be35ff2-2eee-46c2-9c53-30f6ddedbde9)



## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Installation

To run this project, you need to have Python installed along with the Turtle graphics module. Follow the steps below to set up the project on your local machine.

1. Clone the repository:
  
   [git clone] (https://github.com/LakinduNimesh/Turtle-Graphics-Art)
 
2. Navigate to the project directory:
   
   cd turtle-graphics-art
 

## Usage

To run the Turtle graphics code and see the artwork, execute the Python script using the following command:

```sh
python turtle_art.py
```

Make sure you have a Python environment set up on your machine. If you need to install Python, you can download it from [python.org](https://www.python.org/).

Here's a brief overview of the code:

```python
from turtle import *

bgcolor("#000")
speed(0)
pensize(3)

for i in range(9):
    color("#ff0101")
    left(60)
    circle(-18, 200)
    color("#ff0101", "#e8b60f")
    r = 100
    for j in range(12):
        begin_fill()
        circle(r-11*j, 90)
        end_fill()
    left(180)
    penup()
    goto(0,0)
    pendown()

hideturtle()
done()
```

This script sets up a black background and uses nested loops to create a pattern with varying colors and shapes.

## Features

- **Intricate Patterns**: Creates a complex pattern using loops and varying circle sizes.
- **Colorful Design**: Utilizes multiple colors to enhance the visual appeal of the artwork.
- **Fast Rendering**: The `speed(0)` setting ensures the drawing is rendered quickly.

## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact

If you have any questions or suggestions, feel free to reach out:

- **Email**: nimeshlakindu1@gmail.com
- **GitHub**: [LakinduNimesh](https://github.com/LakinduNimesh)

---

Thank you for checking out this Turtle Graphics Art project! Enjoy creating beautiful patterns with Turtle graphics.
```

