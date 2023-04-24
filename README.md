# Forum

Forum is a web application that allows users to create, view, and participate in discussion threads on various topics. It is not jet dedicated to a specific topic

## Installation

To install and run Forum on your local machine, follow these steps:

1. Clone the repository to your computer

    [How to clone a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository?tool=webui)


2. Create a virtual environment

    `python -m venv venv`


3. Enable the virtual environment

    For macOS bash or zsh:

        `source venv/bin/activate`

    [Learn more about virtual environments here](https://docs.python.org/3/library/venv.html)


4. Install requirements in virtual environment

        `pip install -r requirements.txt`


5. Initialize database

        `flask db init`
    
        `flask db upgrade`


6. Create a `.env` file

    It should contain:
        `DATABASE_URL=sqlite:///database.db`
        `FLASK_APP=run.py`
        `SECRET_KEY=` to be defined

        
6. Run the app to see if it is working

        `python run.py`

## Usage

To use Forum, simply create an account or log in to an existing account. You can then browse existing threads or create your own threads on various topics. You can also participate in discussions by replying to existing threads or comments.

## Contributing

We welcome contributions to Forum! If you would like to contribute, please follow these steps:

1. Fork this repository
2. Create a new branch for your changes: `git checkout -b my-new-branch`
3. Make your changes and commit them: `git commit -m "Add new feature"`
4. Push your changes to your forked repository: `git push origin my-new-branch`
5. Submit a pull request to the original repository

Please ensure that your changes follow our coding standards and are thoroughly tested before submitting a pull request.


## Contact Information

If you have any questions or comments, please feel free to contact us by opening an issue on this repository.

## Acknowledgments

Forum uses the following external libraries and resources:

- Flask
- SQLAlchemy

---

