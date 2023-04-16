## FAQs

**Q: What is Quote Engine?**

A: Quote Engine is an API that provides random motivational quotes.

**Q: Do I need an API key to use Quote Engine?**

A: Yes, you need to include your API key in the headers of your API requests to authenticate with the API.

**Q: How do I get an API key?**

A: To get an API key, you need to register for an account on the Quote Engine website and generate an API key from your account dashboard.

**Q: What is the rate limit for API requests?**

A: The rate limit for API requests is currently set at 100 requests per minute. If you exceed this limit, you will receive a 429 error response.

**Q: What format are the quotes returned in?**

A: The quotes are returned in JSON format, with the following fields: `quote` (string) and `author` (string).

**Q: Can I request multiple quotes at once?**

A: Yes, you can specify the number of quotes you want to receive by including a `limit` parameter in your API request. The default value for `limit` is 1 if not specified.

**Q: Is the Quote Engine API free to use?**

A: Yes, the Quote Engine API is free to use for non-commercial purposes. If you plan to use the API for commercial purposes, please contact us to discuss licensing options.
