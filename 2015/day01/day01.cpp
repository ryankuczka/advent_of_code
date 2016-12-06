#include <iostream>
#include <fstream>
#include <string>

int main() {
    int floor_num = 0;
    int first_basement = 0;

    std::string line;
    std::ifstream inp ("input.txt");

    if (inp.is_open()) {
        while (getline(inp, line)) {
            for (int i = 0; i < line.length(); i++) {
                char c = line[i];
                // Update floor num
                if (c == '(') {
                    floor_num++;
                } else {
                    floor_num--;
                }
                // Check for basement
                if (floor_num == -1 && first_basement == 0) {
                    first_basement = i + 1;
                }
            }
        }

        std::cout << "Final Floor: " << floor_num << '\n';
        std::cout << "First Basement: " << first_basement << '\n';
    }
    else std::cout << "Unable to open input.txt";

    return 0;
}
