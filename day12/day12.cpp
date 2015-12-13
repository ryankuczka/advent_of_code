#include <iostream>
#include <fstream>
#include <string>
#include <regex>

int main() {
    int sum = 0;
    int redless = 0;

    std::string line;
    std::ifstream inp ("input.txt");

    if (inp.is_open()) {
        while (getline(inp, line)) {
            std::regex num_regex ("-?\\d+");

            std::regex_iterator<std::string::iterator> found_nums (line.begin(), line.end(), num_regex);
            std::regex_iterator<std::string::iterator> rend;

            while (found_nums != rend) {
                std::string numstr = found_nums->str();
                int num = std::stoi(numstr);
                sum += num;
                found_nums++;
            }
            std::cout << "Sum: " << sum << '\n';
        }
    }
    else std::cout << "Unable to open input.txt";

    return 0;
}
