party_color_dict_germany = {
    "Christian Democratic Union/Christian Social Union": "black",
    "Social Democratic Party of Germany": "red",
    "Free Democratic Party": "yellow",
    "The Greens": "green",
    "Greens/Alliance‘90": "green",
    "Alliance‘90/Greens": "green", # since 93
    "nAlliance‘90/Greens": "green", # Assigning a color for the new combined party
    "Alternative for Germany": "blue",
    "Party of Democratic Socialism": "#AA336A", # 1990-2005
    "The Left. Party of Democratic Socialism": "#AA336A", # 2005-2007
    "The Left": "#AA336A", # since 2007
    "nPDS/The Left": "purple"  # Assigning a color for the new combined party
}

##################404: Economic Planning: Positive adds to L ?

manifesto_coding_dict = {
    # marceco = 401+414
     "per401": "Free Market Economy"
    ,"per402": "Incentives: Positive"
    ,"per407": "Protectionism: Negative"
    ,"per408": "Economic Goals" # 408 raus?
    ,"per410": "Economic Growth: Positive"
    ,"per414": "Economic Orthodoxy positive"
    ,"per702": "Labour Groups: Negative" # 7002 raus?

    ,"per704": "Middle Class and Professional Groups"


    # planeco = 403+404+412
    ,"per403": "Market Regulation"
    ,"per404": "Economic Planning" #408
    ,"per405": "Corporatism/Mixed Economy"
    ,"per409": "Keynesian Demand Management" # or more markeco??
    ,"per412": "Controlled Economy"
    ,"per413": "Nationalisation"
    ,"per415": "Marxist Analysis: Positive"
    ,"per701": "Labour Groups: Positive"
    # 4121, 4124 0.0
    
    # n_crisiseco
    ,"per402": "Incentives: Positive"
    ,"per409": "Keynesian Demand Management"
    ,"per410": "Economic Growth: Positive"
    # -! 414

    # or:
    ,"per416": " Anti-Growth Economy and Sustainability"

    # against welfare
    ,"per505": "Welfare State Limitation"
    ,"per507": "Education Limitation"

    # welfare = 503+504
    ,"per502": "Culture: Positive"
    ,"per503": "Equality: Positive"
    ,"per504": "Welfare State Expansion"
    ,"per506": "Education Expansion"

    # contra Immigration / Multiculturalism
    ,"per601": "National Way of Life: Positive"
    ,"per608": "Multiculturalism: Negative"

    #pro Immigration / Multicalturalism
    ,"per602": "National Way of Life: Negative"
    ,"per607": "Multiculturalism: Positive"
}

all_codes_dict = {
    'per101': 'Foreign Special Relationships: Positive',
    'per102': 'Foreign Special Relationships: Negative',
    'per103': 'Anti-Imperialism',
    'per104': 'Military: Positive',
    'per105': 'Military: Negative',
    'per106': 'Peace',
    'per107': 'Internationalism: Positive',
    'per108': 'European Community/Union: Positive',
    'per109': 'Internationalism: Negative',
    'per110': 'European Community/Union: Negative',
    'per201': 'Freedom and Human Rights',
    'per202': 'Democracy',
    'per203': 'Constitutionalism: Positive',
    'per204': 'Constitutionalism: Negative',
    'per301': 'Decentralization',
    'per302': 'Centralisation',
    'per303': 'Governmental and Administrative Efficiency',
    'per304': 'Political Corruption',
    'per305': 'Political Authority',
    'per401': 'Free Market Economy',
    'per402': 'Incentives: Positive',
    'per403': 'Market Regulation',
    'per404': 'Economic Planning',
    'per405': 'Corporatism/Mixed Economy',
    'per406': 'Protectionism: Positive',
    'per407': 'Protectionism: Negative',
    'per408': 'Economic Goals',
    'per409': 'Keynesian Demand Management',
    'per410': 'Economic Growth: Positive',
    'per411': 'Technology and Infrastructure: Positive',
    'per412': 'Controlled Economy',
    'per413': 'Nationalisation',
    'per414': 'Economic Orthodoxy',
    'per415': 'Marxist Analysis',
    'per416': 'Anti-Growth Economy: Positive',
    'per501': 'Environmental Protection',
    'per502': 'Culture: Positive',
    'per503': 'Equality: Positive',
    'per504': 'Welfare State Expansion',
    'per505': 'Welfare State Limitation',
    'per506': 'Education Expansion',
    'per507': 'Education Limitation',
    'per601': 'National Way of Life: Positive',
    'per602': 'National Way of Life: Negative',
    'per603': 'Traditional Morality: Positive',
    'per604': 'Traditional Morality: Negative',
    'per605': 'Law and Order: Positive',
    'per606': 'Civic Mindedness: Positive',
    'per607': 'Multiculturalism: Positive',
    'per608': 'Multiculturalism: Negative',
    'per701': 'Labour Groups: Positive',
    'per702': 'Labour Groups: Negative',
    'per703': 'Agriculture and Farmers: Positive',
    'per704': 'Middle Class and Professional Groups',
    'per705': 'Underprivileged Minority Groups',
    'per706': 'Non-economic Demographic Groups',
    'rile': 'Right-left position of party',
    'planeco': 'Economic Planning',
    'markeco': 'Market Economy',
    'welfare': 'Welfare',
    'intpeace': 'International Peace'
}
