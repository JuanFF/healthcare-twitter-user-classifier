# health-worker-classifier

This is a text classifier that categorizes user names and descriptions from health worker profiles in Twitter. Twitter users provide information on themselves in their user names and descriptions. This classifier reads from these fiels and returns a descriptive tag for the type of health work profile.

If the input to the classifer is the following text (user name and description from the Twitter profile of the World Health Organization)

<img src = 'https://github.com/JuanFF/health-worker-classifier/blob/master/WHO.png' style="float:left;width:8rem;margin-right:0.7rem"/>

User name is ```WHO```

User description is ```We are the #UnitedNations’ health agency. We are committed to achieving better health for everyone, everywhere - #HealthForAll```

Then, the classifier output tag will be ```Institution```

If the user name or description is not related to healthcare, the classifier output will be ```empty```

This is the complete list of profile tags returned by the classifier:

- Academia
- Publishing source
- Doctor
- Professional
- Medical business
- Interested in healthcare
- News source
- Healthcare initiative
- Association
- Generic


## Installation

Clone this repository with

```bash
git clone https://github.com/JuanFF/health-worker-classifier.git
```
You do not need any additional library. However, you may want to use this classifier with [Tweepy](https://www.tweepy.org), a Python library to access the Twitter API and retrieve user names and description as input data.


## Usage

Use ```run_classifier.py``` to call the function that receives two text strings as input and returns the profile tag as a string.

The function ```run_classifier``` takes two variables as arguments:

```python
run_classifier (user_name, user_description)
```

In the above example, ```user_name``` is ```WHO```and ```user_description``` is ```We are the #UnitedNations’ health agency. We are committed to achieving better health for everyone, everywhere - #HealthForAll```

You can test the classifier from the terminal using ```classifier_test.py``` with strings in quotes as arguments: The first argument is the user name, and the second argument is the user description text.


```bash
test_sentence.py "WHO" "We are the #UnitedNations’ health agency. We are committed to achieving better health for everyone, everywhere"
```

The output will then be ```Institution```
