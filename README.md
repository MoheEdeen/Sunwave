# Sunwave

Sunwave is an application designed to calculate the various aspects needed to install solar panels efficiently. This application provides a user-friendly interface and numerous features to simplify the planning process for solar panel installations. It is built using the Python Kivy library.

## Features

- **Annual Usage Calculation**: Computes the average annual energy usage for your building using limited input data.
- **Power Requirements Estimation**: Determines the power needed to fulfill your energy usage based on the provided data.
- **Solar Panel Requirements**: Calculates the number of solar panels required and their power output based on the specifications of the solar panel you provide.
- **Bearing Load Calculation**: Automatically computes the bearing load to ensure the system is structurally sound.
- **Inverter Suggestions**: Provides options for inverters suitable for your setup.
- **MPPT Count**: Suggests the number of MPPTs (Maximum Power Point Trackers) to assist the engineer in determining the required number of strings.
- **Circuit Breaker Selection**: Calculates the current at which the circuit breaker should trip for safety and suggests suitable circuit breakers.
- **Wire Cross Section Calculation**: Computes the cross-section of the wire (for 2-core wires) based on the wiring details you provide.

## Requirements

The application uses the Python Kivy library and other dependencies listed in `requirements.txt`.

## Installation and Usage

1. Clone the repository or download the source code.
2. Install the required libraries by running:

   ```bash
   pip install -r requirements.txt
   ```

3. Ensure that `main.py` is in the same directory as the other files.
4. Run the application using the following command:

   ```bash
   python main.py
   ```

## Notes

- Make sure all dependencies in `requirements.txt` are installed before running the application.
- This application is designed to provide an estimation and assistance for solar panel installations. Always consult a professional engineer for final validation and implementation.

---

## Images:
![SW1](https://github.com/user-attachments/assets/0d2b27e2-185f-4501-b2e8-9cb91e85e5c8)
![SW2](https://github.com/user-attachments/assets/ebc49bf7-426b-4b04-a0f9-4a0e424a3bce)
![SW3](https://github.com/user-attachments/assets/ebcf05a1-cab2-4b9c-9f2f-23bc4f882e3d)
![SW4](https://github.com/user-attachments/assets/0c50ef95-e4bd-40f2-af38-e2b7662e896b)

Feel free to contribute or report issues to improve this application further!
