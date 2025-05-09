# Agro-Food Tracker

![Agro-Food Tracker Logo](https://github.com/xSSanDev/Quality_Tracker/blob/master/Logo.jpg)

## 🌱 About the Project

Agro-Food Tracker is a smart digital platform designed to help agro-food businesses, cooperatives, and local producers efficiently manage and monitor their product data. Built with Django, this web-based application simplifies the creation, organization, and tracking of essential product information such as name, category, description, price, image, and creation date.

**Live Demo:** [https://anass23.pythonanywhere.com/](https://anass23.pythonanywhere.com/)

## 🎯 Target Users

- Local farmers
- Food cooperatives
- Agro-product entrepreneurs
- Agricultural students and researchers

## 🔍 Problem Statement

Many farmers and small agro-food businesses still rely on manual methods like notebooks and spreadsheets for product management, which are time-consuming and prone to errors. This limits their ability to organize products, maintain accurate data, and grow efficiently. Without simple digital solutions, they struggle with traceability, operational optimization, and market responsiveness, ultimately hindering innovation and business expansion.

## ✨ Features

- **Product Management:** Create, view, edit, and delete products
- **Data Visualization:** Clean and intuitive dashboard interface
- **Export Functionality:** Download product information as CSV files
- **Search & Filter:** Find products by name or category
- **Sorting Options:** Organize products by various criteria
- **Pagination:** Navigate through large product lists with ease
- **Responsive Design:** Works on desktop and mobile devices

## 🛠️ Technologies Used

- **Backend:** Django (Python web framework)
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite (default Django database)
- **Deployment:** PythonAnywhere

## 📋 Project Structure

```
Quality_Tracker/
├── products/                     # Main app directory
│   ├── migrations/               # Database migration files
│   ├── templates/                # HTML templates
│   ├── __init__.py              # Makes directory a Python package
│   ├── admin.py                 # Django admin configuration
│   ├── apps.py                  # App configuration
│   ├── forms.py                 # Form definitions
│   ├── models.py                # Database models
│   ├── tests.py                 # Unit tests
│   ├── urls.py                  # URL routing for this app
│   └── views.py                 # View functions or classes
├── Quality_Tracker/             # Main project directory
│   ├── __init__.py              # Makes directory a Python package
│   ├── asgi.py                  # ASGI deployment
│   ├── settings.py              # Project settings
│   ├── urls.py                  # Main URL routing
│   └── wsgi.py                  # WSGI deployment
├── manage.py                    # Django command-line utility
└── requirements.txt             # Project dependencies
```


## 📸 Screenshots

### Product Dashboard
![Dashboard](https://github.com/xSSanDev/Quality_Tracker/blob/master/product_Dashboard.png)

### Product Creation
![Product Creation](https://github.com/xSSanDev/Quality_Tracker/blob/master/product_creation.png)

### Product Detail View
![Product Detail](https://github.com/xSSanDev/Quality_Tracker/blob/master/detailed_view.png)

## 🌟 Key Functionalities

### Product Management
- Create, view, edit, and delete products
- Upload product images
- Set product categories and prices

### Data Export
- Export product data to CSV format
- Filter exports based on search criteria and categories

### Search and Filter
- Search products by name
- Filter by category
- Sort by newest first
- Pagination for easy navigation

## 👨‍💻 Author

**Anass Zeroual**
- 📚 Biotechnology Agro-food student and emerging software engineer
- 💻 Backend development specialist with Django
- 🔗 [LinkedIn](https://www.linkedin.com/in/anass-zeroual)
- 🌐 [GitHub](https://github.com/xSSanDev)

## 📄 License

This project is licensed under the [MIT License](LICENSE).

## 🙏 Acknowledgements

- Supervised by Pr. Ghizlane Hnini
- Django framework and its community
- All contributors and users of Agro-Food Tracker
