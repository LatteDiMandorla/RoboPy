#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char * read_api(const char * filename) {
  FILE * file = fopen(filename, "r");
  if (!file) {
    fprintf(stderr, "Error\n");
    return NULL;
  }

  char API_KEY[256];
  while(fgets(API_KEY, sizeof(API_KEY), file)) {
    if (strncmp(API_KEY, "API_KEY=", 8) == 0) {
      char * key_start = API_KEY + 8;
      


      char * result = malloc(strlen(key_start) + 1);
      if (result != NULL) {
        strcpy(result, key_start);
      }
      fclose(file);
      return result;
    }

    fclose(file);
    fprintf(stderr, "No API_KEY found\n", filename);
    return NULL;
  }
}


