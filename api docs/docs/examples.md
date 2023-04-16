## EXAMPLES
### javascript fetch
```javascript
const apiURL = 'https://your-quote-engine-api.com/quotes';
const limit = 1; // You can change this to return more quotes if you'd like

fetch(`${apiURL}/random?limit=${limit}`, {
  headers: {
    'X-API-Key': 'your-api-key-here'
  }
})
  .then(response => response.json())
  .then(data => {
    console.log(data); // Log the response to the console
    // Do something with the quote data
    const quote = data[0]; // If `limit` is set to 1, this will get the first (and only) quote
    console.log(quote.quote); // Log the quote text to the console
    console.log(quote.author); // Log the quote author to the console
  })
  .catch(error => {
    console.error(error); // Log any errors to the console
  });

```


### Javascript axios

```javascript
const axios = require('axios');

const API_URL = 'https://example.com/api';
const API_KEY = 'your_api_key';

// Fetch a random quote
const getRandomQuote = async (limit = 1) => {
  try {
    const response = await axios.get(`${API_URL}/random?limit=${limit}`, {
      headers: {
        'x-api-key': API_KEY
      }
    });
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

// Usage example
getRandomQuote().then(data => console.log(data));

```


### python

```python
import requests

API_URL = 'https://example.com/api'
API_KEY = 'your_api_key'

# Fetch a random quote
def get_random_quote(limit=1):
    headers = {'x-api-key': API_KEY}
    params = {'limit': limit}
    response = requests.get(f'{API_URL}/random', headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f'Error fetching quote: {response.status_code}')
        return None

# Usage example
quote = get_random_quote()
if quote:
    print(quote['quote'])
    print(f'- {quote['author']}')

```


### java
```java
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.HashMap;
import java.util.Map;

public class QuoteAPI {
    private static final String API_URL = "https://example.com/api";
    private static final String API_KEY = "your_api_key";

    // Fetch a random quote
    public static String[] getRandomQuote(int limit) throws Exception {
        Map<String, String> headers = new HashMap<>();
        headers.put("x-api-key", API_KEY);

        URI uri = URI.create(API_URL + "/random?limit=" + limit);
        HttpRequest request = HttpRequest.newBuilder()
                .uri(uri)
                .headers(headers.entrySet().stream()
                        .flatMap(e -> e.getValue().isEmpty() ?
                                Stream.empty() :
                                Stream.of(e.getKey(), e.getValue()))
                        .toArray(String[]::new))
                .build();

        HttpResponse<String> response = HttpClient.newHttpClient()
                .send(request, HttpResponse.BodyHandlers.ofString());

        if (response.statusCode() == 200) {
            String[] quote = new String[2];
            quote[0] = response.body().split("\"")[3];
            quote[1] = response.body().split("\"")[7];
            return quote;
        } else {
            System.out.println("Error fetching quote: " + response.statusCode());
            return null;
        }
    }

    // Usage example
    public static void main(String[] args) throws Exception {
        String[] quote = getRandomQuote(1);
        if (quote != null) {
            System.out.println(quote[0]);
            System.out.println("- " + quote[1]);
        }
    }
}

```

### dart
```dart
import 'dart:convert';
import 'package:http/http.dart' as http;

Future<Map<String, dynamic>> getRandomQuote({int limit = 1, String apiKey}) async {
  final url = Uri.parse('https://example.com/api/random?limit=$limit');
  final response = await http.get(
    url,
    headers: {'x-api-key': apiKey},
  );
  
  if (response.statusCode == 200) {
    final data = jsonDecode(response.body);
    final quote = data['quote'];
    final author = data['author'];
    return {'quote': quote, 'author': author};
  } else {
    throw Exception('Failed to fetch quote');
  }
}

// Usage example
void main() async {
  final apiKey = 'your_api_key';
  final quote = await getRandomQuote(apiKey: apiKey);
  print('${quote['quote']}\n- ${quote['author']}');
}

```

### php
```php
function getRandomQuote($apiKey, $limit = 1) {
    $url = "https://example.com/api/random?limit=$limit";
    $curl = curl_init($url);
    curl_setopt($curl, CURLOPT_HTTPHEADER, array('x-api-key: ' . $apiKey));
    curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
    $response = curl_exec($curl);
    if(curl_errno($curl)) {
        throw new Exception('Failed to fetch quote: ' . curl_error($curl));
    }
    $httpCode = curl_getinfo($curl, CURLINFO_HTTP_CODE);
    curl_close($curl);
    if($httpCode === 200) {
        $data = json_decode($response, true);
        return array('quote' => $data['quote'], 'author' => $data['author']);
    } else {
        throw new Exception('Failed to fetch quote');
    }
}

// Usage example
$apiKey = 'your_api_key';
$quote = getRandomQuote($apiKey);
echo "{$quote['quote']}\n- {$quote['author']}";

```

### ruby 
```ruby
require 'httparty'

def get_random_quote(api_key, limit = 1)
  url = "https://example.com/api/random?limit=#{limit}"
  headers = {'x-api-key' => api_key}
  response = HTTParty.get(url, headers: headers)
  if response.code == 200
    data = JSON.parse(response.body)
    {'quote' => data['quote'], 'author' => data['author']}
  else
    raise "Failed to fetch quote (status code: #{response.code})"
  end
end

# Usage example
api_key = 'your_api_key'
quote = get_random_quote(api_key)
puts "#{quote['quote']}\n- #{quote['author']}"

```