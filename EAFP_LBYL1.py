import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

person = {
    "name": "ali",
    "age": None
}

# LBYL: Look Before You Leap.
if person.get("age"):
    if person.get("age") < 10:
        print("little man!")

# EAFP: Easier to Ask Forgiveness than Permission.
try:
    if person.get("age") < 10:
        print("little man!")
except Exception as error:
    logger.error(error)

print("hi there")
