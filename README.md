# College Mapper

## Purpose
The purpose of this project is to create a web application to allow people to search for colleges and college information in an easy-to-use map interface. They should be able to save colleges they like, and add relevant times for things like application due-dates to keep track of their college process.

## How to Run

To run for development, you must start the server and run the client. The server allows you to retrieve the necessary data, and the client enables you to see the app itself.

If you haven't already:
* [Install Python](https://realpython.com/installing-python/)
* [Install Node.js (comes with NPM)](https://nodejs.org/en/download/)
* [Install Yarn](https://classic.yarnpkg.com/en/docs/install/#mac-stable)

### Running the Server
Navigate into the API directory:
` cd api 	`

Install the required packages:
`pip install -r requirements.txt`
(**Note:** Depending on the setup of your system, you may need to use `pip3`)

Run the server.
`python3 main.py`
(Server runs on `localhost:5000`)

### Running the Client (Website):
Navigate into the client directory:
`cd client`

Install the packages and run:
`yarn && yarn start`

The website will be up and running on `localhost: 3000` by default.

## Contributing to Front End
To build a component (like a calendar, button, etc.) you should use [storybook](https://storybook.js.org/docs/react/get-started/introduction). Run this using `yarn storybook` (after completing the previous installation steps.) On `localhost: 6006`, you will see a storybook with the different components.

Your component will be made in the `components` file, under its own folder. Once you create a `[component name].stories.js` file, you can see a preview of your component in the storybook.


## Getting Help
If you need help getting the project running, contact Nathaniel on Facebook Messenger or email tamsopensource@gmail.com.
