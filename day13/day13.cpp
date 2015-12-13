#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <regex>
#include <map>
#include <iterator>

int main() {
    std::string line;
    std::ifstream inp ("input.txt");

    std::regex line_regex ("^([A-GM]\\w+) would (gain|lose) (\\d+) happiness units by sitting next to ([A-GM]\\w+)\\.");

    std::map<std::string,std::map<std::string,int>> happiness;

    std::string names[] {"Alice", "Bob", "Carol", "David", "Eric", "Frank", "George", "Mallory"};
    std::string me_names[] {"Alice", "Bob", "Carol", "David", "Eric", "Frank", "George", "Mallory", "Me"};
    int indices[] {0, 1, 2, 3, 4, 5, 6, 7};
    int me_indices[] {0, 1, 2, 3, 4, 5, 6, 7, 8};
    int size = sizeof(indices)/sizeof(indices[0]);
    int me_size = sizeof(me_indices)/sizeof(me_indices[0]);

    if (inp.is_open()) {
        while (getline(inp, line)) {
            std::smatch sm;
            std::regex_match(line, sm, line_regex);

            int diff;
            if (sm[2] == "gain") {
                diff = std::stoi(sm[3]);
            } else {
                diff = std::stoi(sm[3]) * -1;
            }

            happiness[sm[1]][sm[4]] = diff;
        }
    }
    else std::cout << "Unable to open input.txt";

    for (int i = 0; i < 8; i++) {
        happiness[names[i]]["Me"] = 0;
        happiness["Me"][names[i]] = 0;
    }

    int max_happiness = 0;
    do {
        int happiness_lvl = 0;
        for (int i = 0; i < 8; i++) {
            std::string name1 = names[indices[i]];
            std::string name2 = names[indices[(i + 1) % 8]];

            happiness_lvl += happiness[name1][name2];
            happiness_lvl += happiness[name2][name1];
        }
        if (happiness_lvl > max_happiness) {
            max_happiness = happiness_lvl;
        }
    } while (std::next_permutation(indices, indices+size));

    int me_happiness = 0;
    do {
        int happiness_lvl = 0;
        for (int i = 0; i < 9; i++) {
            std::string name1 = me_names[me_indices[i]];
            std::string name2 = me_names[me_indices[(i + 1) % 9]];

            happiness_lvl += happiness[name1][name2];
            happiness_lvl += happiness[name2][name1];
        }
        if (happiness_lvl > me_happiness) {
            me_happiness = happiness_lvl;
        }
    } while (std::next_permutation(me_indices, me_indices+me_size));

    std::cout << "Max Happiness: " << max_happiness << std::endl;
    std::cout << "Me Happiness: " << me_happiness << std::endl;

    return 0;
}
