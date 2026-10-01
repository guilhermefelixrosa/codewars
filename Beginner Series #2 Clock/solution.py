def past(h, m, s):
    # Good Luck!
    h_passed = h*60*60*1000
    m_passed = m*60*1000
    s_passed = s*1000
    time_passed = h_passed + m_passed + s_passed
    return time_passed