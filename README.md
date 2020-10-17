## Vue + Django App Skeleton

## Requirements

- npm
- vue-cli
- pip
- python3
- python-dev-tools


## Build Setup

Before installing the dependencies, create a virtualenv with

1. Install dependencies
    ```shell script
    make install
    ```
2. Configure datasets
    ```shell script
    make seed
    ```

## Running on dev

1. Inside the project python environment, run the django server
    ```shell script
    make run-backend
    ```

2. In another terminal windown run the npm hot reloader serve
    ```shell script
    make run-frontend
    ```

### New project setup

Execute the following script to generate a django token:

```shell script
python generate_key.py
```

Copy the output code into the the `app.settings.base.SECRET_KEY` var value.

The index.html file is loaded in the `/` path by the `app.urls` and it
bootstraps the vue application inside the `src.main`.

The `src.App` loads the vue app and its associated `src.components`.
