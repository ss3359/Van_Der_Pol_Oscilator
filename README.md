# Van_Der_Pol_Oscilator
This project simulates a two dimensional Van Der Pol oscillator, a non-linear system with applications in physics, biology and electrical engineering. The animation shows how the `x(t)` and `y(t)` positions evolve over time using a Runge-Kutta 4th-order integration scheme. A fading trail effect visually represents the path history of the particle.

## Equations Overview
These are the following equations expressing the Van-Der-Pol motion:
                x''(t) - μ(1 - x²)x'(t) + x(t) = 0
                y''(t) = -μ(1 - x²)y'(t) - y(t)

These are expressed as a system of first-order ODEs and solved numerically using the fourth order Runge-Kutta Method.

##  Features

- RK4 integration scheme
- Configurable parameters (`μ`, step size, initial conditions)
- Smooth 2D animation with trailing path
- Modular class design (`VanDerPol`)
