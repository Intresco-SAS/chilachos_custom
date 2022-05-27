
{
	'name': 'Rodbal-Chilacos',
	
	'version': '12.0',
       
	'summary': 'Rodbal - Customization',
	'description': """
Plantillas de Reportes Colombia:
======================
	* Este módulo realiza unos ajustes a distintas vistas para que sea mas facil la operación de los administradores.
	
	""",
	'depends': [
		
		'account','purchase','purchase_stock','stock'
	],
	'data': [
		'views/purchase_view_custom.xml',
	],
	'installable': True,
	'application': True,
}
