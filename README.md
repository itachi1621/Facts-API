# Random Fact API

Welcome to the Random Fact API, a simple FastAPI-based web service that provides random facts on demand. This API is designed to be lightweight, easy to use, and a fun way to learn something new with just a simple API call.

![FastAPI Logo](https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png)

## Getting Started

### Prerequisites

- Python 3.7 or later
- [FastAPI](https://fastapi.tiangolo.com/) installed. If not, you can install it using:
- Uvicorn
- Gunicorn (if serving via nginx )

## To install all required packages use
  ```
 pip install -r requirements.txt

```

## To run locally once installed use
```
uvicorn FactsAPI:app --reload
```

## Endpoints

###Demo endpoint

```
https://facts.zerosystems.org/api/v1/intresting/fact
```

#### Documentation
```
127.0.0.1/docs

```

#### Version
```
127.0.0.1/version
```


#### Useless fact
```
127.0.0.1/api/v1/useless/fact

```

#### Useless fact with specific id
```
127.0.0.1/api/v1/useless/fact?fid=1

```

#### Intresting fact
```
127.0.0.1/api/v1/intresting/fact

```

#### Intresting fact with id
```
127.0.0.1/api/v1/intresting/fact?fid=1
