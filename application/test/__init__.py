{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 106,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_excel(\"EURO.xls\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>curs</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>822.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>19.804639</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>0.548949</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>19.089000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>19.429200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>19.621200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>20.040200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>21.342600</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             curs\n",
       "count  822.000000\n",
       "mean    19.804639\n",
       "std      0.548949\n",
       "min     19.089000\n",
       "25%     19.429200\n",
       "50%     19.621200\n",
       "75%     20.040200\n",
       "max     21.342600"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "19.804639294403874"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df [\"curs\"].mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "df [\"curs_ban\"] = df [\"curs\"] * 100"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>data</th>\n",
       "      <th>curs</th>\n",
       "      <th>curs_ban</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2018-11-30</td>\n",
       "      <td>19.5868</td>\n",
       "      <td>1958.68</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2018-12-01</td>\n",
       "      <td>19.5868</td>\n",
       "      <td>1958.68</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2018-12-02</td>\n",
       "      <td>19.5868</td>\n",
       "      <td>1958.68</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2018-12-03</td>\n",
       "      <td>19.5479</td>\n",
       "      <td>1954.79</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2018-12-04</td>\n",
       "      <td>19.4373</td>\n",
       "      <td>1943.73</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>817</th>\n",
       "      <td>2021-02-24</td>\n",
       "      <td>21.3035</td>\n",
       "      <td>2130.35</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>818</th>\n",
       "      <td>2021-02-25</td>\n",
       "      <td>21.2724</td>\n",
       "      <td>2127.24</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>819</th>\n",
       "      <td>2021-02-26</td>\n",
       "      <td>21.3426</td>\n",
       "      <td>2134.26</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>820</th>\n",
       "      <td>2021-02-27</td>\n",
       "      <td>21.3426</td>\n",
       "      <td>2134.26</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>821</th>\n",
       "      <td>2021-02-28</td>\n",
       "      <td>21.3426</td>\n",
       "      <td>2134.26</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>822 rows × 3 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "          data     curs  curs_ban\n",
       "0   2018-11-30  19.5868   1958.68\n",
       "1   2018-12-01  19.5868   1958.68\n",
       "2   2018-12-02  19.5868   1958.68\n",
       "3   2018-12-03  19.5479   1954.79\n",
       "4   2018-12-04  19.4373   1943.73\n",
       "..         ...      ...       ...\n",
       "817 2021-02-24  21.3035   2130.35\n",
       "818 2021-02-25  21.2724   2127.24\n",
       "819 2021-02-26  21.3426   2134.26\n",
       "820 2021-02-27  21.3426   2134.26\n",
       "821 2021-02-28  21.3426   2134.26\n",
       "\n",
       "[822 rows x 3 columns]"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "Matplotlib is building the font cache; this may take a moment.\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "df[\"curs\"].plot()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [],
   "source": [
    "money = df[\"curs\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "money.plot()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "past = 7 * 4 # interval in trecut\n",
    "future = 7 # interval prognozat "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "822"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(money)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [],
   "source": [
    "start = past \n",
    "end = len (money) - future"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [],
   "source": [
    "raw_df = []\n",
    "for i in range(start,end):\n",
    "    past_and_future_values = money[(i-past):(i+future)]\n",
    "    raw_df.append(list(past_and_future_values))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [],
   "source": [
    "past_columns = []\n",
    "for i in range (past):\n",
    "    past_columns.append(\"past_{}\".format(i))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [],
   "source": [
    "future_columns = []\n",
    "for i in range (future):\n",
    "    future_columns.append(\"future_{}\".format(i))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.DataFrame(raw_df, columns=(past_columns+future_columns))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>past_0</th>\n",
       "      <th>past_1</th>\n",
       "      <th>past_2</th>\n",
       "      <th>past_3</th>\n",
       "      <th>past_4</th>\n",
       "      <th>past_5</th>\n",
       "      <th>past_6</th>\n",
       "      <th>past_7</th>\n",
       "      <th>past_8</th>\n",
       "      <th>past_9</th>\n",
       "      <th>...</th>\n",
       "      <th>past_25</th>\n",
       "      <th>past_26</th>\n",
       "      <th>past_27</th>\n",
       "      <th>future_0</th>\n",
       "      <th>future_1</th>\n",
       "      <th>future_2</th>\n",
       "      <th>future_3</th>\n",
       "      <th>future_4</th>\n",
       "      <th>future_5</th>\n",
       "      <th>future_6</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>19.5868</td>\n",
       "      <td>19.5868</td>\n",
       "      <td>19.5868</td>\n",
       "      <td>19.5479</td>\n",
       "      <td>19.4373</td>\n",
       "      <td>19.5029</td>\n",
       "      <td>19.4431</td>\n",
       "      <td>19.4881</td>\n",
       "      <td>19.4881</td>\n",
       "      <td>19.4881</td>\n",
       "      <td>...</td>\n",
       "      <td>19.8353</td>\n",
       "      <td>19.7167</td>\n",
       "      <td>19.5835</td>\n",
       "      <td>19.5212</td>\n",
       "      <td>19.5212</td>\n",
       "      <td>19.5212</td>\n",
       "      <td>19.5212</td>\n",
       "      <td>19.5212</td>\n",
       "      <td>19.6191</td>\n",
       "      <td>19.5679</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>19.5868</td>\n",
       "      <td>19.5868</td>\n",
       "      <td>19.5479</td>\n",
       "      <td>19.4373</td>\n",
       "      <td>19.5029</td>\n",
       "      <td>19.4431</td>\n",
       "      <td>19.4881</td>\n",
       "      <td>19.4881</td>\n",
       "      <td>19.4881</td>\n",
       "      <td>19.5740</td>\n",
       "      <td>...</td>\n",
       "      <td>19.7167</td>\n",
       "      <td>19.5835</td>\n",
       "      <td>19.5212</td>\n",
       "      <td>19.5212</td>\n",
       "      <td>19.5212</td>\n",
       "      <td>19.5212</td>\n",
       "      <td>19.5212</td>\n",
       "      <td>19.6191</td>\n",
       "      <td>19.5679</td>\n",
       "      <td>19.5230</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>19.5868</td>\n",
       "      <td>19.5479</td>\n",
       "      <td>19.4373</td>\n",
       "      <td>19.5029</td>\n",
       "      <td>19.4431</td>\n",
       "      <td>19.4881</td>\n",
       "      <td>19.4881</td>\n",
       "      <td>19.4881</td>\n",
       "      <td>19.5740</td>\n",
       "      <td>19.6490</td>\n",
       "      <td>...</td>\n",
       "      <td>19.5835</td>\n",
       "      <td>19.5212</td>\n",
       "      <td>19.5212</td>\n",
       "      <td>19.5212</td>\n",
       "      <td>19.5212</td>\n",
       "      <td>19.5212</td>\n",
       "      <td>19.6191</td>\n",
       "      <td>19.5679</td>\n",
       "      <td>19.5230</td>\n",
       "      <td>19.5230</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>19.5479</td>\n",
       "      <td>19.4373</td>\n",
       "      <td>19.5029</td>\n",
       "      <td>19.4431</td>\n",
       "      <td>19.4881</td>\n",
       "      <td>19.4881</td>\n",
       "      <td>19.4881</td>\n",
       "      <td>19.5740</td>\n",
       "      <td>19.6490</td>\n",
       "      <td>19.6229</td>\n",
       "      <td>...</td>\n",
       "      <td>19.5212</td>\n",
       "      <td>19.5212</td>\n",
       "      <td>19.5212</td>\n",
       "      <td>19.5212</td>\n",
       "      <td>19.5212</td>\n",
       "      <td>19.6191</td>\n",
       "      <td>19.5679</td>\n",
       "      <td>19.5230</td>\n",
       "      <td>19.5230</td>\n",
       "      <td>19.5230</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>19.4373</td>\n",
       "      <td>19.5029</td>\n",
       "      <td>19.4431</td>\n",
       "      <td>19.4881</td>\n",
       "      <td>19.4881</td>\n",
       "      <td>19.4881</td>\n",
       "      <td>19.5740</td>\n",
       "      <td>19.6490</td>\n",
       "      <td>19.6229</td>\n",
       "      <td>19.5436</td>\n",
       "      <td>...</td>\n",
       "      <td>19.5212</td>\n",
       "      <td>19.5212</td>\n",
       "      <td>19.5212</td>\n",
       "      <td>19.5212</td>\n",
       "      <td>19.6191</td>\n",
       "      <td>19.5679</td>\n",
       "      <td>19.5230</td>\n",
       "      <td>19.5230</td>\n",
       "      <td>19.5230</td>\n",
       "      <td>19.5230</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>782</th>\n",
       "      <td>21.0309</td>\n",
       "      <td>21.0955</td>\n",
       "      <td>21.1921</td>\n",
       "      <td>21.1921</td>\n",
       "      <td>21.1921</td>\n",
       "      <td>21.2947</td>\n",
       "      <td>21.2242</td>\n",
       "      <td>21.0973</td>\n",
       "      <td>21.0295</td>\n",
       "      <td>20.9355</td>\n",
       "      <td>...</td>\n",
       "      <td>21.2129</td>\n",
       "      <td>21.1373</td>\n",
       "      <td>21.1127</td>\n",
       "      <td>21.1510</td>\n",
       "      <td>20.9748</td>\n",
       "      <td>21.0745</td>\n",
       "      <td>21.0745</td>\n",
       "      <td>21.0745</td>\n",
       "      <td>21.3067</td>\n",
       "      <td>21.3054</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>783</th>\n",
       "      <td>21.0955</td>\n",
       "      <td>21.1921</td>\n",
       "      <td>21.1921</td>\n",
       "      <td>21.1921</td>\n",
       "      <td>21.2947</td>\n",
       "      <td>21.2242</td>\n",
       "      <td>21.0973</td>\n",
       "      <td>21.0295</td>\n",
       "      <td>20.9355</td>\n",
       "      <td>20.9355</td>\n",
       "      <td>...</td>\n",
       "      <td>21.1373</td>\n",
       "      <td>21.1127</td>\n",
       "      <td>21.1510</td>\n",
       "      <td>20.9748</td>\n",
       "      <td>21.0745</td>\n",
       "      <td>21.0745</td>\n",
       "      <td>21.0745</td>\n",
       "      <td>21.3067</td>\n",
       "      <td>21.3054</td>\n",
       "      <td>21.3035</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>784</th>\n",
       "      <td>21.1921</td>\n",
       "      <td>21.1921</td>\n",
       "      <td>21.1921</td>\n",
       "      <td>21.2947</td>\n",
       "      <td>21.2242</td>\n",
       "      <td>21.0973</td>\n",
       "      <td>21.0295</td>\n",
       "      <td>20.9355</td>\n",
       "      <td>20.9355</td>\n",
       "      <td>20.9355</td>\n",
       "      <td>...</td>\n",
       "      <td>21.1127</td>\n",
       "      <td>21.1510</td>\n",
       "      <td>20.9748</td>\n",
       "      <td>21.0745</td>\n",
       "      <td>21.0745</td>\n",
       "      <td>21.0745</td>\n",
       "      <td>21.3067</td>\n",
       "      <td>21.3054</td>\n",
       "      <td>21.3035</td>\n",
       "      <td>21.2724</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>785</th>\n",
       "      <td>21.1921</td>\n",
       "      <td>21.1921</td>\n",
       "      <td>21.2947</td>\n",
       "      <td>21.2242</td>\n",
       "      <td>21.0973</td>\n",
       "      <td>21.0295</td>\n",
       "      <td>20.9355</td>\n",
       "      <td>20.9355</td>\n",
       "      <td>20.9355</td>\n",
       "      <td>21.0099</td>\n",
       "      <td>...</td>\n",
       "      <td>21.1510</td>\n",
       "      <td>20.9748</td>\n",
       "      <td>21.0745</td>\n",
       "      <td>21.0745</td>\n",
       "      <td>21.0745</td>\n",
       "      <td>21.3067</td>\n",
       "      <td>21.3054</td>\n",
       "      <td>21.3035</td>\n",
       "      <td>21.2724</td>\n",
       "      <td>21.3426</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>786</th>\n",
       "      <td>21.1921</td>\n",
       "      <td>21.2947</td>\n",
       "      <td>21.2242</td>\n",
       "      <td>21.0973</td>\n",
       "      <td>21.0295</td>\n",
       "      <td>20.9355</td>\n",
       "      <td>20.9355</td>\n",
       "      <td>20.9355</td>\n",
       "      <td>21.0099</td>\n",
       "      <td>20.9071</td>\n",
       "      <td>...</td>\n",
       "      <td>20.9748</td>\n",
       "      <td>21.0745</td>\n",
       "      <td>21.0745</td>\n",
       "      <td>21.0745</td>\n",
       "      <td>21.3067</td>\n",
       "      <td>21.3054</td>\n",
       "      <td>21.3035</td>\n",
       "      <td>21.2724</td>\n",
       "      <td>21.3426</td>\n",
       "      <td>21.3426</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>787 rows × 35 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "      past_0   past_1   past_2   past_3   past_4   past_5   past_6   past_7  \\\n",
       "0    19.5868  19.5868  19.5868  19.5479  19.4373  19.5029  19.4431  19.4881   \n",
       "1    19.5868  19.5868  19.5479  19.4373  19.5029  19.4431  19.4881  19.4881   \n",
       "2    19.5868  19.5479  19.4373  19.5029  19.4431  19.4881  19.4881  19.4881   \n",
       "3    19.5479  19.4373  19.5029  19.4431  19.4881  19.4881  19.4881  19.5740   \n",
       "4    19.4373  19.5029  19.4431  19.4881  19.4881  19.4881  19.5740  19.6490   \n",
       "..       ...      ...      ...      ...      ...      ...      ...      ...   \n",
       "782  21.0309  21.0955  21.1921  21.1921  21.1921  21.2947  21.2242  21.0973   \n",
       "783  21.0955  21.1921  21.1921  21.1921  21.2947  21.2242  21.0973  21.0295   \n",
       "784  21.1921  21.1921  21.1921  21.2947  21.2242  21.0973  21.0295  20.9355   \n",
       "785  21.1921  21.1921  21.2947  21.2242  21.0973  21.0295  20.9355  20.9355   \n",
       "786  21.1921  21.2947  21.2242  21.0973  21.0295  20.9355  20.9355  20.9355   \n",
       "\n",
       "      past_8   past_9  ...  past_25  past_26  past_27  future_0  future_1  \\\n",
       "0    19.4881  19.4881  ...  19.8353  19.7167  19.5835   19.5212   19.5212   \n",
       "1    19.4881  19.5740  ...  19.7167  19.5835  19.5212   19.5212   19.5212   \n",
       "2    19.5740  19.6490  ...  19.5835  19.5212  19.5212   19.5212   19.5212   \n",
       "3    19.6490  19.6229  ...  19.5212  19.5212  19.5212   19.5212   19.5212   \n",
       "4    19.6229  19.5436  ...  19.5212  19.5212  19.5212   19.5212   19.6191   \n",
       "..       ...      ...  ...      ...      ...      ...       ...       ...   \n",
       "782  21.0295  20.9355  ...  21.2129  21.1373  21.1127   21.1510   20.9748   \n",
       "783  20.9355  20.9355  ...  21.1373  21.1127  21.1510   20.9748   21.0745   \n",
       "784  20.9355  20.9355  ...  21.1127  21.1510  20.9748   21.0745   21.0745   \n",
       "785  20.9355  21.0099  ...  21.1510  20.9748  21.0745   21.0745   21.0745   \n",
       "786  21.0099  20.9071  ...  20.9748  21.0745  21.0745   21.0745   21.3067   \n",
       "\n",
       "     future_2  future_3  future_4  future_5  future_6  \n",
       "0     19.5212   19.5212   19.5212   19.6191   19.5679  \n",
       "1     19.5212   19.5212   19.6191   19.5679   19.5230  \n",
       "2     19.5212   19.6191   19.5679   19.5230   19.5230  \n",
       "3     19.6191   19.5679   19.5230   19.5230   19.5230  \n",
       "4     19.5679   19.5230   19.5230   19.5230   19.5230  \n",
       "..        ...       ...       ...       ...       ...  \n",
       "782   21.0745   21.0745   21.0745   21.3067   21.3054  \n",
       "783   21.0745   21.0745   21.3067   21.3054   21.3035  \n",
       "784   21.0745   21.3067   21.3054   21.3035   21.2724  \n",
       "785   21.3067   21.3054   21.3035   21.2724   21.3426  \n",
       "786   21.3054   21.3035   21.2724   21.3426   21.3426  \n",
       "\n",
       "[787 rows x 35 columns]"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Invatare\n",
    "\n",
    "x = df[past_columns] [:-20]\n",
    "y = df[future_columns] [:-20]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Verificare\n",
    "\n",
    "x_test = df[past_columns] [-20:]\n",
    "y_test = df[future_columns] [-20:]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.linear_model import LinearRegression"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [],
   "source": [
    "LinReg = LinearRegression()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "LinearRegression()"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "LinReg.fit(x, y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [],
   "source": [
    "prediction = LinReg.predict(x_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[21.00375473, 21.00353937, 20.98166043, 20.98790403, 20.97964868,\n",
       "        20.98709561, 20.95987736],\n",
       "       [20.90823806, 20.88684065, 20.89733246, 20.88755703, 20.90125464,\n",
       "        20.87562749, 20.90395763],\n",
       "       [20.81984458, 20.83198626, 20.82619368, 20.83948146, 20.81737261,\n",
       "        20.8452411 , 20.87626668],\n",
       "       [20.90192314, 20.89723425, 20.90670819, 20.88604103, 20.90905512,\n",
       "        20.93899148, 20.90175433],\n",
       "       [20.88601436, 20.89719498, 20.87839234, 20.90217841, 20.93183326,\n",
       "        20.89400876, 20.8774241 ],\n",
       "       [20.90094941, 20.88345496, 20.90606678, 20.93598693, 20.89780821,\n",
       "        20.8815043 , 20.88661742],\n",
       "       [20.86746824, 20.88815022, 20.91317772, 20.87246937, 20.85969571,\n",
       "        20.86690782, 20.8628198 ],\n",
       "       [20.97477655, 21.01218945, 20.98750849, 20.98635527, 20.97734431,\n",
       "        20.966707  , 20.95366962],\n",
       "       [21.09459638, 21.07021359, 21.06592196, 21.05868641, 21.04230676,\n",
       "        21.02845796, 21.01560766],\n",
       "       [21.2091563 , 21.20679739, 21.19431031, 21.18144725, 21.15742404,\n",
       "        21.14309615, 21.12460535],\n",
       "       [21.25553976, 21.24463757, 21.22926924, 21.20657084, 21.18851787,\n",
       "        21.16896941, 21.15565379],\n",
       "       [21.20597386, 21.19298882, 21.17437924, 21.15711986, 21.13857239,\n",
       "        21.12463955, 21.11907032],\n",
       "       [21.20283544, 21.18624876, 21.17043463, 21.15332463, 21.13746392,\n",
       "        21.13123312, 21.12368699],\n",
       "       [21.19786329, 21.1830276 , 21.16900206, 21.15470073, 21.14620362,\n",
       "        21.13735326, 21.11353816],\n",
       "       [21.12972282, 21.12004097, 21.11374726, 21.10735522, 21.09873237,\n",
       "        21.07293152, 21.04915544],\n",
       "       [21.09937856, 21.0908568 , 21.07687273, 21.06472905, 21.04381738,\n",
       "        21.02318964, 20.97923334],\n",
       "       [21.1433947 , 21.13055303, 21.11482559, 21.09499029, 21.07094856,\n",
       "        21.02746916, 21.00158937],\n",
       "       [20.96120293, 20.94402304, 20.92509303, 20.89552209, 20.86585717,\n",
       "        20.84280258, 20.87476253],\n",
       "       [21.05993154, 21.04363981, 21.01118464, 20.98530258, 20.95302158,\n",
       "        20.98413785, 20.94895919],\n",
       "       [21.06280689, 21.03341039, 21.00856006, 20.97818924, 21.00631789,\n",
       "        20.96937075, 20.96274721]])"
      ]
     },
     "execution_count": 58,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "prediction"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([21.06280689, 21.03341039, 21.00856006, 20.97818924, 21.00631789,\n",
       "       20.96937075, 20.96274721])"
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "prediction[19]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>future_0</th>\n",
       "      <th>future_1</th>\n",
       "      <th>future_2</th>\n",
       "      <th>future_3</th>\n",
       "      <th>future_4</th>\n",
       "      <th>future_5</th>\n",
       "      <th>future_6</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>786</th>\n",
       "      <td>21.0745</td>\n",
       "      <td>21.3067</td>\n",
       "      <td>21.3054</td>\n",
       "      <td>21.3035</td>\n",
       "      <td>21.2724</td>\n",
       "      <td>21.3426</td>\n",
       "      <td>21.3426</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     future_0  future_1  future_2  future_3  future_4  future_5  future_6\n",
       "786   21.0745   21.3067   21.3054   21.3035   21.2724   21.3426   21.3426"
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y_test [-1:]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.legend.Legend at 0x107443b3d30>"
      ]
     },
     "execution_count": 87,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.plot(prediction[2], label=\"prediction\")\n",
    "plt.plot(y_test[-18:].iloc[0], label=\"real\")\n",
    "plt.legend()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.metrics import mean_absolute_error"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.09177403301334865"
      ]
     },
     "execution_count": 88,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mean_absolute_error(y_test[-18:].iloc[0], prediction[5])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "metadata": {},
   "outputs": [],
   "source": [
    "def printErrors(prediction):\n",
    "    errors_list = []\n",
    "    for i in range (len (prediction)):\n",
    "        error = mean_absolute_error (y_test.iloc[i], prediction[i])\n",
    "        errors_list.append(error)\n",
    "    avg_err = sum(errors_list) / len (errors_list)\n",
    "    max_err = max(errors_list)\n",
    "    print(\"eroarea medie = {}\".format(avg_err))\n",
    "    print(\"eroarea maxima = {}\".format(max_err))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "eroarea medie = 0.142552787302982\n",
      "eroarea maxima = 0.30031951855399186\n"
     ]
    }
   ],
   "source": [
    "printErrors(prediction)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.neural_network import MLPRegressor"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "metadata": {},
   "outputs": [],
   "source": [
    "MLP = MLPRegressor()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "MLPRegressor()"
      ]
     },
     "execution_count": 96,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "MLP.fit(x,y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "metadata": {},
   "outputs": [],
   "source": [
    "predictionMLP = MLP.predict(x_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "eroarea medie = 0.15662750450308072\n",
      "eroarea maxima = 0.27816918420744685\n"
     ]
    }
   ],
   "source": [
    "printErrors(predictionMLP)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 124,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.neighbors import KNeighborsRegressor"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 139,
   "metadata": {},
   "outputs": [],
   "source": [
    "KNN = KNeighborsRegressor(n_neighbors=45)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 140,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "KNeighborsRegressor(n_neighbors=45)"
      ]
     },
     "execution_count": 140,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "KNN.fit(x,y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 141,
   "metadata": {},
   "outputs": [],
   "source": [
    "predictionKNN = KNN.predict(x_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 142,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "eroarea medie = 0.13238933333333253\n",
      "eroarea maxima = 0.2233174603174563\n"
     ]
    }
   ],
   "source": [
    "printErrors(predictionKNN)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 143,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.legend.Legend at 0x10744c02b80>"
      ]
     },
     "execution_count": 143,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.plot(predictionKNN[19], label=\"predictionKNN\")\n",
    "plt.plot(y_test[-1:].iloc[0], label=\"real\")\n",
    "plt.legend()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import GridSearchCV"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "MLP = MLPRegressor(hidden_layer_sizes=(100,100,100))\n",
    "GSCV = GridSearchCV (MLP, {\n",
    "    \"max_iter\": [100,500,1000],\n",
    "    \"learning_rate_init\": [0.001, 0.01],\n",
    "},  cv=3, scoring ='explained_variance')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "GSCV.fit(x,y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "GSCV.best_estimator_"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
