
## Usage

You will need to setup an `.env` file with the following variables:

`LLM_API_KEY`: Can be either OpenAI key, Claude key or any other LLM provider key. (See LiteLLM docs above for full info on supported LLMs)

`LLM_MODEL`: The model you want to use. (See LiteLLM docs above for full info on supported LLMs)

Scraper keys: they're optional, but if not provided, you will need to scrape and pass the HTMLs to Oxy® Parser yourself.
However, we highly suggest to use Oxylabs scraper since it will remove the hassle of getting HTMLs and will also
provide you with a lot of other benefits like rotating IPs, handling captchas, bypassing blocks.

Click here to sign up for Oxylabs free trial: https://dashboard.oxylabs.io/en/registration?productToBuy=SCRAPI_WEB

`OXYLABS_SCRAPER_USER`: Your Oxylabs scraper user (optional)
`OXYLABS_SCRAPER_PASSWORD`: Your Oxylabs scraper password (optional)

```env
LLM_API_KEY=your_openai_api_key
LLM_MODEL=gpt-3.5-turbo
OXYLABS_SCRAPER_USER=your_oxylabs_scraper_user  # optional
OXYLABS_SCRAPER_PASSWORD=your_oxylabs_scraper_pass  # optional
```
