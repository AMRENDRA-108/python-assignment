{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "7936849e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter your number10\n"
     ]
    }
   ],
   "source": [
    " number = int(input(\"enter your number\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "05e2ba99",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Even number\n"
     ]
    }
   ],
   "source": [
    "if number%2 == 0:\n",
    "    print(\"Even number\");\n",
    "else:\n",
    "    print(\"Odd number\");"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "23c6be73",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "3\n",
      "6\n",
      "10\n",
      "15\n",
      "21\n",
      "28\n",
      "36\n",
      "45\n",
      "55\n",
      "66\n",
      "78\n",
      "91\n",
      "105\n",
      "120\n",
      "136\n",
      "153\n",
      "171\n",
      "190\n",
      "210\n",
      "231\n",
      "253\n",
      "276\n",
      "300\n",
      "325\n",
      "351\n",
      "378\n",
      "406\n",
      "435\n",
      "465\n",
      "496\n",
      "528\n",
      "561\n",
      "595\n",
      "630\n",
      "666\n",
      "703\n",
      "741\n",
      "780\n",
      "820\n",
      "861\n",
      "903\n",
      "946\n",
      "990\n",
      "1035\n",
      "1081\n",
      "1128\n",
      "1176\n",
      "1225\n",
      "1275\n"
     ]
    }
   ],
   "source": [
    "sum = 0;\n",
    "for i in range(1,51):\n",
    "   \n",
    "    sum = sum + i; \n",
    "    print(sum)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0eb440fb",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
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
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
