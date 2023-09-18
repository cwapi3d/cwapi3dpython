---
hide:
  - toc
---

# Compare

## compare floats

```python

if __name__ == '__main__':
    a: float = 1.23
    b: float = 1.230000000001

    print("numbers are equal") if (a == b) else print("numbers are different")
    result: bool = abs(a - b) < 1e-4
    print(result)

```

## compare strings

```python
if __name__ == '__main__':
    print("cadwork" == "cadwork")
    print("Cadwork" < "cadwork")
    print("Cadwork" > "cadwork")
    print("cadwork" != "cadwork")

#output
# True
# True
# False
# False
```

### compare objects

```python
import dataclasses

# value class
@dataclasses.dataclass()
class Address:
    street: str
    number: int
    zipcode: int

    def __eq__(self, other):
        if not isinstance(other, Address):
            return False
        return self.street == other.street \
            and self.number == other.number \
            and self.zipcode == other.zipcode

# entity class
class Person:
    def __init__(self, name, passport_id, address):
        self.name: str = name
        self.address: Address = address
        self.passport_id: int = passport_id

    def __eq__(self, other):
        if not isinstance(other, Person):
            return False
        return self.passport_id == other.passport_id

    def __hash__(self):
        return hash(self.passport_id)


if __name__ == '__main__':
    address1 = Address(street="ThisStreet", number=20, zipcode=8084)
    address2 = Address(street="OtherStreet", number=204, zipcode=9000)

    print(address1 == address2)

    person1 = Person(name="John", passport_id=123456, address=address1)
    person2 = Person(name="John", passport_id=123456, address=address2)

    print(person1 == person2)
    print(person1.__hash__() == person2.__hash__())

```
