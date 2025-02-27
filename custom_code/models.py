from django.db import models
from tom_targets.base_models import BaseTarget
# 
# 
class MicrolensingTarget(BaseTarget):
    """
    Microlensing Target fields.   
    """
 
    # OPM-specific microlensing fields
    classification = models.CharField(max_length=50, default='Microlensing PSPL')
    # model parameters from a broker or any other source providing fits    
    t0 = models.FloatField(default=0)
    u0 = models.FloatField(default=0)
    tE = models.FloatField(default=0)
    # parameters from gaia
    gaia_source_id = models.CharField(max_length=30, default='', null=True, blank=True)
    gmag = models.FloatField(default=0)
    gmag_error = models.FloatField(default=0)
    rpmag = models.FloatField(default=0)
    rpmag_error = models.FloatField(default=0)
    bpmag = models.FloatField(default=0)
    bpmag_error = models.FloatField(default=0)
    bprp = models.FloatField(default=0)
    bprp_error = models.FloatField(default=0)
    reddening_bprp = models.FloatField(default=0)
    extinction_g = models.FloatField(default=0)
    teff = models.FloatField(default=0)
    logg = models.FloatField(default=0)
    metallicity = models.FloatField(default=0)
    ruwe = models.FloatField(default=0)
    broker_priority = models.FloatField(default=0)
    lasair_classification = models.CharField(max_length=120, default='', null=True, blank=True)
    alerce_classification = models.CharField(max_length=120, default='', null=True, blank=True)
    alerce_classification_probability = models.CharField(default=0)
    fink_classification = models.CharField(max_length=120, default='', null=True, blank=True)
    fink_classification_probability = models.CharField(default=0)
    
    ruwe = models.FloatField(default=0)
    class Meta:
         verbose_name = "target"
         permissions = (
             ('view_target', 'View Target'),
             ('add_target', 'Add Target'),
             ('change_target', 'Change Target'),
             ('delete_target', 'Delete Target'),
         )

