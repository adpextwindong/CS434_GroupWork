if __name__ == '__main__':
    csv_header = []
    for label in ['time','glucose','slope','iob','mob','morning','afternoon','evening','night']:
        for i in range(7):
            csv_header.append(
                't' + str(i) + '_' + label
            )

    print csv_header

# Dimensions to drop
# morning, afternoon, evening, night
#