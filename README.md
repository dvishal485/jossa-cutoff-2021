# jossa-cutoff-2021
JoSAA 2021 Opening and Closing Ranks spreadhseet file(s) &amp; pdf(s) along with a short analysis

#### Disclaimer
I am not affliated to JoSSA or any other body by any means. All data here is taken from official sources and is for educational purpose only.

---

## Downloads
Opening and Closing Rank for JoSAA 2021 Round 6 :
- [Excel Document](./josaa-cutoff.xlsx)
- [Portable Document Format (PDF)](./josaa.pdf)
- [Google Sheets](https://docs.google.com/spreadsheets/d/1ftV86BdXwuJKV58S08wyNd9QfdTVxciJeu6GJ1CaDMg/edit?usp=sharing)

---

## Generate on your own
All the information on Opening & Closing Ranks are taken from official [JoSAA Webpage](https://josaa.nic.in/Counseling/seatallotmentresult/currentorcr.aspx)

For generating excel file from other set of data follow these instructions :

1. Clone the repository on your system

    `git clone https://github.com/dvishal485/jossa-cutoff-2021.git`
1. Open the [JoSAA Opening & Closing Ranks Webpage](https://josaa.nic.in/Counseling/seatallotmentresult/currentorcr.aspx)
1. Submit all the information in the form to view all data you need in webpage
1. Hit <kbd>Ctrl</kbd>+<kbd>s</kbd> and save the whole page as HTML as `JoSAA.html` (will probably be the default name)
1. Move the saved `JoSAA.html` into the root directory of repository cloned on your system
1. Run [main.py](./main.py) in the root folder
    
    `python main.py`
1. A new `josaa-cutoff.xlsx` will be saved in the root folder.

---

# License & Copyright

  - This Project is [Apache-2.0](./LICENSE) Licensed
  - Copyright 2021 [Vishal Das](https://github.com/dvishal485)
