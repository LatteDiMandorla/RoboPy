#include <stdio.h>
#include <stdlib.h>
#include <string.h> 
#include <curl/curl.h>

void send_hi(const char * furhat_ip, const char *text) {
  /* curl is a pointer to libcurl session, res will store the result of 
   * request. */ 

  CURL * curl;
  CURLcode res;
  

  /* snprintf transforms url in the right string. */ 

  char url[256];
  snprintf(url, sizeof(url), "http://%s/api/say", furhat_ip);

  char json[512];
  snprintf(json, sizeof(json), "{\"text\": \"%s\"}", text);

  curl = curl_easy_init();
  if (curl) {
    struct curl_slist * headers = NULL; 

    headers = curl_slist_append(headers, "Content-Type: application/json");
    
    /* This part set:
     * - where to send the request.
     * - which headers to use.
     * - body of POST request.      */

    curl_easy_setopt(curl, CURLOPT_URL, url);
    curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);
    curl_easy_setopt(curl, CURLOPT_POSTFIELDS, json);

    res = curl_easy_perform(curl);
  
    if (res != CURLE_OK) {
      fprintf(stderr, "Error in the request: %s\n", curl_easy_strerror(res));
    }

    /* Let's clear all memory. */ 

    curl_slist_free_all(headers);
    curl_easy_cleanup(curl);
  }
}
