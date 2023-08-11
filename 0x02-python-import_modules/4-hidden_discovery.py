#!/usr/bin/python3

if __name__ == "__main__":
    
    import hidden_4 as mode

    values = dir(mode)
    for value in values:
        if value[:2] != "__":
            print(value)
