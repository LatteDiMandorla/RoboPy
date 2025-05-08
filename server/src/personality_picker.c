#include "personality_picker.h"
#include <stdio.h> 
#include <stdlib.h>
#include <string.h>
#include <cjson/cJSON.h>
#include <stdbool.h>


void create_prompt(const char * text){
  FILE * file = fopen("../prompt/prompt.txt", "a");

  if (file == NULL) { 
    fprintf(stderr, "Error opening file!\n");
    return;
  }

  fprintf(file, "%s", text);
  fclose(file);

}

/* Parsing the jSON file sent by the client, in order to 
 * decide which personality has the user, and behave conseguentally. */ 

void parse_jSON(int client_socket, char buffer[]){
  const cJSON * extraversion      = NULL;
  const cJSON * agreeableness     = NULL;
  const cJSON * conscientiousness = NULL;
  const cJSON * stability         = NULL;
  const cJSON * openness          = NULL;


  cJSON * json = cJSON_Parse(buffer);
  
  if (json == NULL) {
    fprintf(stderr, "Error into jSON parsing\n");
    cJSON_Delete(json)
    close(client_socket);
    return;
  }

  extraversion      = cJSON_GetObjectItemCaseSensitive(json, "Estroversione");
  agreeableness     = cJSON_GetObjectItemCaseSensitive(json, "Amicalità");
  conscientiousness = cJSON_GetObjectItemCaseSensitive(json, "Coscienziosità");
  stability         = cJSON_GetObjectItemCaseSensitive(json, "Stabilità");
  openness          = cJSON_GetObjectItemCaseSensitive(json, "Apertura");

  if (!cJSON_IsNumber(extraversion)      || 
      !cJSON_IsNumber(agreeableness)     ||
      !cJSON_IsNumber(conscientiousness) ||
      !cJSON_IsNumber(stability)         ||
      !cJSON_IsNumber(openness))          {

    fprintf(stderr, "Some data is invalid\n");
    return;

  }

}


void decide_personality(const cJSON * first_value, 
                        const cJSON * second_value, 
                        const cJSON * third_value, 
                        const cJSON * fourth_value,
                        const cJSON * fifth_value) {
  
  int extr_value = first_value->valueint;
  int agre_value = second_value->valueint;
  int conc_value = third_value->valueint;
  int stab_value = fourth_value->valueint;
  int open_value = fifth_value->valueint;

  /* If the score is a number between 2 and 14, we can say that 8 is minimum number
   * to consider the user positive. The function write an important information about 
   * the personality into a prompt.txt and store it. */ 

  if (extr_value >= 8) { create_prompt("\n-Estroverso\n");      }
  else                 { create_prompt("\n-Introverso\n");      }

  if (agre_value >= 8) { create_prompt("\n-Amichevole\n");      }
  else                 { create_prompt("\n-Scontroso\n");       }

  if (conc_value >= 8) { create_prompt("\n-Coscenzioso\n");     }
  else                 { create_prompt("\n-Impulsivo\n");       }

  if (stab_value >= 8) { create_prompt("\n-Stabile\n");         }
  else                 { create_prompt("\n-Instabile\n");       }

  if (open_value >= 8) { create_prompt("\n-Aperto di mente\n"); }
  else                 { create_prompt("\n-Chiuso di mente\n"); }

}


