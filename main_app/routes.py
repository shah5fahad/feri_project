from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("homepage.html")


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/peer_reviewed')
def peer_reviewed():
    return render_template('peer_reviewed.html')


@app.route('/ugc_care')
def ugc_care():
    return render_template('ugc_care.html')


@app.route('/DOI_Allocation')
def DOI_Allocation():
    return render_template('DOI_Allocation.html')


@app.route('/Payment')
def Payment():
    return render_template('Payment.html')

@app.route('/global_trade_climate_invasive_species')
def global_trade_climate_invasive_species():
    return render_template('global_trade_climate_invasive_species.html')


@app.route('/current_issue')
def current_issue():
    return render_template('Current_issue.html')


@app.route('/runjh_dam_biodiversity')
def runjh_dam_biodiversity():
    return render_template('runjh_dam_biodiversity.html')


@app.route('/genetic_fidelity')
def genetic_fidelity():
    return render_template('genetic_fidelity.html')


@app.route('/bamboo_shoots_research')
def bamboo_shoots_research():
    return render_template('bamboo_shoots_research.html')


@app.route('/leucistic_starling')
def leucistic_starling():
    return render_template('leucistic_starling.html')



@app.route('/urban_sprawl_narsinghgarh')
def urban_sprawl_narsinghgarh():
    return render_template('urban_sprawl_narsinghgarh.html')

@app.route('/group')
def group():
    return render_template('group.html')
