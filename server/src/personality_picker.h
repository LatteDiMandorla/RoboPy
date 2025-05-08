#ifndef PERSONALITY_PICKER
#define PERSONALITY_PICKER

#include <cjson/cJSON.h>

void create_prompt(char * text);

void parse_jSON(int client_socket, char buffer[]);

void decide_personality(const cJSON * first_value, 
                        const cJSON * second_value, 
                        const cJSON * third_value, 
                        const cJSON * fourth_value,
                        const cJSON * fifth_value);

#endif
