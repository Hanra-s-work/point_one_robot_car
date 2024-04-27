#include <iostream>
#include <string>
#include <cmath>
#include <vector>
#include <random>
#include "alglib/src/stdafx.h"
#include "alglib/src/interpolation.h"
// #include "matplotlibcpp.h"

// namespace plt = matplotlibcpp;

// void visualize_spline(std::vector<double> &x, std::vector<double> &y, alglib::spline1dinterpolant &s)
// {
//     // Generate x values for plotting the spline
//     std::vector<double> x_plot;

//     for (double i = x.front(); i <= x.back(); i += 10000)
//         x_plot.push_back(i);

//     // Calculate corresponding y values using the spline
//     std::vector<double> y_plot(x_plot.size());

//     for (size_t i = 0; i < x_plot.size(); ++i)
//         y_plot[i] = alglib::spline1dcalc(s, x_plot[i]);

//     // Plot the data
//     plt::plot(x, y, "o");
//     plt::plot(x_plot, y_plot, "-");
//     plt::title("Piecewise Linear Spline Interpolation");
//     plt::legend();
//     plt::show();
// }

void sort_vector(std::vector<double> &vec1, std::vector<double> &vec2)
{
    std::vector<double> sortedVec1;
    std::vector<double> sortedVec2;
    std::size_t index = 0;

    while (!vec1.empty()) {
        index = 0;
        for (std::size_t i = 1; i < vec1.size(); i++) {
            if (vec1[index] > vec1[i]) {
                index = i;
            }
        }
        sortedVec1.push_back(vec1[index]);
        vec1.erase(vec1.begin() + index);
        sortedVec2.push_back(vec2[index]);
        vec2.erase(vec2.begin() + index);
    }
    vec1 = sortedVec1;
    vec2 = sortedVec2;
}

int spline(std::vector<double> &x, std::vector<double> &y)
{
    sort_vector(x, y);

    try {
        alglib::real_1d_array x_alglib;
        alglib::real_1d_array y_alglib;
        alglib::spline1dinterpolant s;
        alglib::barycentricinterpolant p;
        alglib::real_1d_array a;

        // Set x and y for alglib
        x_alglib.setcontent(x.size(), x.data());
        y_alglib.setcontent(y.size(), y.data());

        // build cubic spline
        alglib::spline1dbuildcubic(x_alglib, y_alglib, s);

        // Generate barycentric interpolant
        alglib::polynomialbuild(x_alglib, y_alglib, p);

        // Convert to power
        alglib::polynomialbar2pow(p, a);
    } catch(alglib::ap_error alglib_exception) {
        printf("ALGLIB exception with message '%s'\n", alglib_exception.msg.c_str());
        return 1;
    }
    return 0;
}

int main(void)
{
    std::vector<double> x;
    std::vector<double> y;

    x.push_back(8500); y.push_back(7000); // A
    x.push_back(5000); y.push_back(7000); // B
    x.push_back(1500); y.push_back(7000); // C
    x.push_back(650); y.push_back(6500); // D
    x.push_back(500); y.push_back(6000); // E
    x.push_back(500.1); y.push_back(5424.5); // F
    x.push_back(650.1); y.push_back(4849); // G
    x.push_back(1500.1); y.push_back(4349); // H
    x.push_back(3400); y.push_back(4349); // I
    x.push_back(4250); y.push_back(3850); // J
    x.push_back(4400); y.push_back(3424.5); // K
    x.push_back(4400.1); y.push_back(2700); // L
    x.push_back(4250.1); y.push_back(2075.5); // M
    x.push_back(3400.1); y.push_back(1787.5); // N
    x.push_back(2766.7); y.push_back(2075.5); // O
    x.push_back(2133); y.push_back(2700); // P
    x.push_back(1500.2); y.push_back(3062.25); // Q
    x.push_back(650.2); y.push_back(2700); // R
    x.push_back(500.2); y.push_back(2075.5); // S
    x.push_back(500.3); y.push_back(1500); // T
    x.push_back(650.3); y.push_back(1000); // U
    x.push_back(1500.3); y.push_back(500); // V
    x.push_back(5000.1); y.push_back(500); // W
    x.push_back(6600.1); y.push_back(500); // X
    x.push_back(8500.1); y.push_back(500); // Y
    x.push_back(9350); y.push_back(1000); // Z
    x.push_back(9500); y.push_back(1500); // A2
    x.push_back(9500.1); y.push_back(2075.5); // B2
    x.push_back(9350.1); y.push_back(2700); // C2
    x.push_back(8500.2); y.push_back(3100); // D2
    x.push_back(6600.2); y.push_back(3100); // E2
    x.push_back(5750); y.push_back(3424.5); // F2
    x.push_back(5500); y.push_back(4075.5); // G2
    x.push_back(5500.1); y.push_back(4800); // H2
    x.push_back(5750.1); y.push_back(5424.5); // I2
    x.push_back(6600.3); y.push_back(5900); // J2
    x.push_back(7450); y.push_back(5424.5); // K2
    x.push_back(7850); y.push_back(4800); // L2
    x.push_back(8500.3); y.push_back(4350); // M2
    x.push_back(9350.2); y.push_back(4800); // N2
    x.push_back(9500.2); y.push_back(5424.5); // O2
    x.push_back(9500.3); y.push_back(6000); // P2
    x.push_back(9350.3); y.push_back(6500); // Q2

    return spline(x, y);
}
