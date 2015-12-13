#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <regex>

int main() {
    std::string line;
    std::ifstream inp ("input.txt");

    std::regex line_regex ("(\\d+)x(\\d+)x(\\d+)");

    int area = 0;
    int ribbon = 0;

    if (inp.is_open()) {
        while (getline(inp, line)) {
            std::smatch sm;
            std::regex_match(line, sm, line_regex);

            int x = std::stoi(sm[1]);
            int y = std::stoi(sm[2]);
            int z = std::stoi(sm[3]);

            int dims[] {x, y, z};
            std::sort(std::begin(dims), std::end(dims));

            int a = x * y;
            int b = x * z;
            int c = y * z;
            int sides[] {a, b, c};
            std::sort(std::begin(sides), std::end(sides));

            // Add surface area of present
            area += 2 * a + 2 * b + 2 * c;

            // Add smallest side
            area += sides[0];

            // Add two smallest dimensions
            ribbon += 2 * dims[0];
            ribbon += 2 * dims[1];

            // Add volume
            ribbon += x * y * z;
        }
    }
    else std::cout << "Unable to open input.txt";

    std::cout << "Wrapping Paper: " << area << std::endl;
    std::cout << "Ribbon: " << ribbon << std::endl;

    return 0;
}
