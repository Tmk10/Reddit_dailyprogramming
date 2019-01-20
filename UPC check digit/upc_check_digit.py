def upc(upc):
    upc = [int(char) for char in "{:011d}".format(upc)]
    m_number = (sum(upc[::2]) * 3 + sum(upc[1::2])) % 10
    return m_number if m_number == 0 else 10 - m_number
