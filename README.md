# Client Churn Prediction

## Detecting TopBank customers' churn probability

#### This project was made by Bruno Schirmer.

# 1. Business Problem.

TopBank is a large banking company. It operates mainly in European countries offering financial products, from bank accounts to investments, including some types of insurance and investment products.

The company's business model is of the service type, that is, it sells banking services to its customers through physical branches and an online portal.

The company's main product is a bank account, in which the customer can deposit his salary, make withdrawals, deposits and transfer to other accounts. This bank account has no cost to the customer and is valid for 12 months, that is, the customer needs to renew the contract for this account to continue using it for the next 12 months.

According to TopBank's Analytics team, each customer who has this bank account returns a monetary amount of 15% of their estimated salary amount, if it is less than average, and 20% if this salary is greater than average, during the current period of your account. This amount is calculated annually.

For example, if a customer's monthly salary is R$1,000.00 and the average of all bank salaries is R$800. The company, therefore, invoices R$ 200 annually with this customer. If this customer has been with the bank for 10 years, the company has already earned R$2,000.00 from transactions and account usage.

In recent months, the Analytics team has noticed that the rate of customers canceling their accounts and leaving the bank has reached unprecedented numbers in the company. Concerned about the increase in this rate, the team devised an action plan to reduce customer evasion rate.

Concerned about the drop in this metric, TopBottom's Analytics team hired you as a Data Science consultant to create an action plan, with the objective of reducing customer evasion, that is, preventing the customer from canceling their contract and not renew it for another 12 months. This evasion, in business metrics, is known as Churn.

Generally speaking, Churn is a metric that indicates the number of customers who canceled the contract or stopped buying your product in a certain period of time. For example, customers who canceled the service contract or after it expired, did not renew, are considered churn customers.

Another example would be customers who have not made a purchase for more than 60 days. These customers can be considered churn customers until a purchase is made. The 60-day period is completely arbitrary and varies between companies.

# 2. The challenge.

As a Data Science Consultant, you need to create an action plan to decrease the number of churn customers and show the financial return on your solution.

At the end of your consultancy, you need to deliver to the TopBottom CEO a model in production, which will receive a customer base via API and return that same base “scored”, that is, one more column with the probability of each customer entering into churn.

In addition, you will need to provide a report of the performance of your model and the financial impact of your solution. Questions that the CEO and the Analytics team would like to see in their report:

1. What is TopBank's current Churn rate? How does it vary monthly?
1. Qual a Performance do modelo em classificar os clientes como churns?
1. What is the expected return, in terms of revenue, if the company uses its model to avoid churn from customers?

A possible action to prevent the customer from churning is to offer a discount coupon, or some other financial incentive for him to renew his contract for another 12 months.

Which customers would you give the financial incentive to and what would that amount be, in order to maximize ROI (Return on Investment). Recalling that the sum of the incentives for each client cannot exceed EUR 10,000.00.


# 3. The data

The data used to make the TopBank Data Science project was taken from the competition website [Kaggle](https://www.kaggle.com). To access the original data use the [link](https://www.kaggle.com/mervetorkan/churndataset).

Each row represents a customer and each column contains some attributes that describe that customer. The data set includes information about

* **RowNumber:** O número da coluna
* **CustomerID:** Identificador único do cliente
* **Surname:** Sobrenome do cliente.
* **CreditScore:** A pontuação de Crédito do cliente para o mercado de consumo.
* **Geography:** O país onde o cliente reside.
* **Gender:** O gênero do cliente.
* **Age:** A idade do cliente.
* **Tenure:** Número de anos que o cliente permaneceu ativo.
* **Balance:** Valor monetário que o cliente tem em sua conta bancária.
* **NumOfProducts:** O número de produtos comprado pelo cliente.
* **HasCrCard:** Indica se o cliente possui ou não cartão de crédito.
* **IsActiveMember:** Indica se o cliente fez pelo menos uma movimentação na conta bancário dentro de 12 meses.
* **EstimateSalary:** Estimativa do salário mensal do cliente.
* **Exited:** Indica se o cliente está ou não em Churn.

**Step 01. Data Description:**

**Step 02. Feature Engineering:**

**Step 03. Data Filtering:**

**Step 04. Exploratory Data Analysis:**

**Step 05. Data Preparation:**

**Step 06. Feature Selection:**

**Step 07. Machine Learning Modelling:**

**Step 08. Hyperparameter Fine Tunning:**

**Step 09. Convert Model Performance to Business Values:**

**Step 10. Deploy Modelo to Production:**

# 4. Top 3 Data Insights

**Hypothesis 01:**

**True/False.**

**Hypothesis 02:**

**True/False.**

**Hypothesis 03:**

**True/False.**

# 5. Machine Learning Model Applied

# 6. Machine Learning Modelo Performance

# 7. Business Results

# 8. Conclusions

# LICENSE

# All Rights Reserved - Comunidade DS 2022
