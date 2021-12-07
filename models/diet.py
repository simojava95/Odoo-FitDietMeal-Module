from odoo import models, fields, api


class DietFacts_product_template(models.Model):
    _inherit = 'product.template'
    calories = fields.Integer(string='Calories')
    servingsize = fields.Float("Serving size")
    lastupdate = fields.Date("Last update")
    # dietitem = fields.Boolean('Diet Item')
    nutrient_ids = fields.One2many('product.template.nutrient','product_id','Nutrient')


class DietFacts_res_users_meal(models.Model):
    _name = "res.users.meal"
    _description = "Diet Facts"
    name = fields.Char('Meal Name')
    meal_date = fields.Datetime('Meal Date')
    user_id = fields.Many2one('res.partner', 'Meal User')
    notes = fields.Text('Meal Notes')
    item_ids = fields.One2many('res.users.mealitem', 'meal_id')

    @api.one
    @api.depends('item_ids', 'item_ids.servings')
    def _calcalories(self):
        currentcalories = 0
        for mealitem in self.item_ids:
            currentcalories = currentcalories + (mealitem.calories * mealitem.servings)
        self.totalcalories = currentcalories

    totalcalories = fields.Integer(string='Total Meal Calories', store=True, compute='_calcalories')


class DietFacts_res_users_mealitems(models.Model):
    _name = "res.users.mealitem"
    meal_id = fields.Many2one('res.users.meal')
    item_id = fields.Many2one('product.template', 'Meal Items')
    servings = fields.Float('Serving')
    notes = fields.Text('Meal Item Notes')
    calories = fields.Integer(related='item_id.calories', string='Calories per serving', store=True, readonly=True)


class DietFacts_product_nutient(models.Model):
    _name = 'product.nutrient'
    name = fields.Char('Nutrient Name')
    Uom_id = fields.Many2one('uom.uom', 'Unite of Measure')
    description = fields.Text('Description')


class DietFacts_product_template_nutrient(models.Model):
    _name = 'product.template.nutrient'
    nutrient_id = fields.Many2one('product.nutrient', string='Nutrient')
    product_id = fields.Many2one('product.template', string='Diet item')
    value = fields.Float('value/100g')
    dialypercentage = fields.Float('Dialy Percentage')
    unityofmeasure = fields.Char(related="nutrient_id.Uom_id.name",string="Unity of measure",readonly=True)

