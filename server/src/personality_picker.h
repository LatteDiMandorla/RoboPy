#ifndef PERSONALITY_PICKER
#define PERSONALITY_PICKER

#include <cjson/cJSON.h>

void create_prompt(const char * text);

char * parse_jSON(const char * buffer);

cJSON * decide_personality(const cJSON * first_value, 
                        const cJSON * second_value, 
                        const cJSON * third_value, 
                        const cJSON * fourth_value,
                        const cJSON * fifth_value);

#endif
