{
    'name': 'yourHome Theme',
    'description': 'yourHome website theme',
    'category': 'Theme',
    'sequence': 10,
    'version': '1.0',
    'depends': ['website'],
    'data': [
        # 'data/generate_primary_template.xml',
        'security/ir.model.access.csv',
        'views/header.xml',
        'views/footer.xml',
        'views/homepage.xml',
        'views/cours_page.xml',
        'views/menu.xml',
        'views/bibliotheque.xml',
        'views/yh_document.xml',
        'views/snippets/learning_property.xml',
        'views/snippets/cours_properties.xml',
        'views/snippets/snippets.xml',
        'views/snippets/mega_menu_services.xml',
    ],
    'assets':{
        'web.assets_frontend':[
            'theme_yourHome/static/src/scss/style.scss',
            'theme_yourHome/static/src/scss/homePageStyle.scss',
            'theme_yourHome/static/src/scss/coursPageStyle.scss',
            'theme_yourHome/static/src/scss/learning_property.scss'
        ],
        'web._assets_primary_variables': [
            "theme_yourHome/static/src/scss/primary_variables.scss",
        ]
    },
    'images': [
        # 'static/description/cover.png',
        # 'static/description/theme_default_screenshot.jpg',
    ],
    'configurator_snippets': {
        # 'homepage': ['s_cover', 's_text_image', 's_numbers'],
        # 'about_us': ['s_text_image', 's_image_text', 's_title', 's_company_team'],
        # 'our_services': ['s_three_columns', 's_quotes_carousel', 's_references'],
        # 'pricing': ['s_comparisons'],
        # 'privacy_policy': ['s_faq_collapse'],
    },
    # 'application': False,
    # 'auto_install': False,
    'license': 'LGPL-3',
}
