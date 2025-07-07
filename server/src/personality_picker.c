#include "personality_picker.h"
#include <stdio.h> 
#include <stdlib.h>
#include <string.h>
#include <cjson/cJSON.h>
#include <stdbool.h>
#include <unistd.h>


const char * prompt = "Ti chiami RoboPY. Rispondi solo contestualmente alla conversazione dell'utente. Rispondi brevemente, tenendo in conto che l'utente è:\n";

/* Parsing the jSON file sent by the client, in order to 
 * decide which personality has the user, and behave conseguentally. */ 

char * parse_jSON(const char * buffer){
  const cJSON * extraversion      = NULL;
  const cJSON * agreeableness     = NULL;
  const cJSON * conscientiousness = NULL;
  const cJSON * stability         = NULL;
  const cJSON * openness          = NULL;

  cJSON * json = cJSON_Parse(buffer);
  if (json == NULL) {
    fprintf(stderr, "Error into JSON parsing\n");
    return NULL;  // non serve cJSON_Delete(json) se json è NULL
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
      !cJSON_IsNumber(openness)) {
    cJSON_Delete(json);
    fprintf(stderr, "Some data is invalid\n");
    return NULL;
  }

  cJSON * traits = decide_personality(extraversion, agreeableness, conscientiousness, stability, openness);
  cJSON * response = cJSON_CreateObject();
  if (response == NULL) {
    cJSON_Delete(json);
    if (traits) cJSON_Delete(traits);
    fprintf(stderr, "Failed to create response object\n");
    return NULL;
  }

  cJSON_AddStringToObject(response, "prompt base", "Rispondi solo contestualmente alla conversazione dell'utente, tenendo in conto che l'utente è:\n");

  if (traits != NULL) {
    cJSON_AddItemToObject(response, "personalità", traits);
    // ATTENZIONE: traits ora è "owned" da response, NON cancellarla dopo
  } else {
    cJSON_AddStringToObject(response, "error", "Decide personality failed");
  }

  char * response_string = cJSON_PrintUnformatted(response);

  cJSON_Delete(response);
  cJSON_Delete(json);

  return response_string;
}


cJSON * decide_personality(const cJSON * first_value, 
                        const cJSON * second_value, 
                        const cJSON * third_value, 
                        const cJSON * fourth_value,
                        const cJSON * fifth_value) {
  
  int extr_value = first_value->valueint;
  int agre_value = second_value->valueint;
  int conc_value = third_value->valueint;
  int stab_value = fourth_value->valueint;
  int open_value = fifth_value->valueint;


  cJSON * traits = cJSON_CreateArray();

  /* If the score is a number between 2 and 14, we can say that 8 is minimum number
   * to consider the user positive. The function write an important information about 
   * the personality into a prompt.txt and store it. */ 

  if (extr_value >= 8) { cJSON_AddItemToArray(traits, cJSON_CreateString("Estroverso"));      }
  else                 { cJSON_AddItemToArray(traits, cJSON_CreateString("Introverso"));      }

  if (agre_value >= 8) { cJSON_AddItemToArray(traits, cJSON_CreateString("Amichevole"));      }
  else                 { cJSON_AddItemToArray(traits, cJSON_CreateString("Scontroso"));       }

  if (conc_value >= 8) { cJSON_AddItemToArray(traits, cJSON_CreateString("Coscienzioso"));     }
  else                 { cJSON_AddItemToArray(traits, cJSON_CreateString("Impulsivo"));       }

  if (stab_value >= 8) { cJSON_AddItemToArray(traits, cJSON_CreateString("Stabile"));         }
  else                 { cJSON_AddItemToArray(traits, cJSON_CreateString("Instabile"));       }

  if (open_value >= 8) { cJSON_AddItemToArray(traits, cJSON_CreateString("Aperto di mente")); }
  else                 { cJSON_AddItemToArray(traits, cJSON_CreateString("Chiuso di mente")); }


  return traits;

}

