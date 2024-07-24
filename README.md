# scape_tools
Useful tools, maybe.


# Wordlist statistics counter
example: 
python3 wordlist_counter.py /usr/share/wordlists/seclists/Passwords/xato-net-10-million-passwords-10000.txt 

expected output:
Check the length of entries in the file - /usr/share/wordlists/seclists/Passwords/xato-net-10-million-passwords-10000.txt

Length <6: 814  8%
Length  6: 904  9%
Length  7: 3176 32%
Length  8: 1770 18%
Length  9: 2972 30%
Length 10: 218  2%
Length 11: 94   1%
Length 12: 28   0%
Length 13: 21   0%
Length 14: 1    0%
Length>14: 2    0%

_____ _____ _____ _____ _____ _____ _____ _____ _____ _____

Check for charset in each entry

wordlist counter: 10000

special  counter: 12    0%
upper    counter: 114   1%
lower    counter: 7987  80%
decimal  counter: 2818  28%
