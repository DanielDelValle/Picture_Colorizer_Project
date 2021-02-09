{
 "metadata": {
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": 3
  },
  "orig_nbformat": 2
 },
 "nbformat": 4,
 "nbformat_minor": 2,
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def show_html(html_str):\n",
    "    print(BeautifulSoup(str(html_str), 'html.parser').prettify())\n",
    "\n",
    "def get_page_contents(url):\n",
    "    page = requests.get(url, headers={\"Accept-Language\": \"en-US\"})\n",
    "    return BeautifulSoup(page.text, \"html.parser\")"
   ]
  }
 ]
}