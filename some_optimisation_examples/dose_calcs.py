import numpy as np
from matplotlib import pyplot as plt

"""
the plan for this was to demonstrate linear optimization of fluence in a very simple
'patient'.
But, it's not finished. Maybe next time!!
"""

class Patient:
    """
    describes a 2D square patient made of water with a circular PTV in the middle!
    """
    def __init__(self, patient_size=31):
        self.patient_size = patient_size  # size in voxels. make it odd always!!
        assert self.patient_size % 2 == 1
        self.linear_attenuation_coefficient = .1
        self.PTV_radius = 7
        self._generate_coordinates()
        self._generate_patient()

    def _generate_coordinates(self):

        bounds = np.floor(self.patient_size/2)
        self.x = np.linspace(-bounds, bounds, self.patient_size)
        self.y = np.linspace(-bounds, bounds, self.patient_size)
        [self.X, self.Y] = np.meshgrid(self.x, self.y)

    def _generate_patient(self):
        """
        create a 2D matrix representing patient
        we will use zeros to represent healthy tissue and ones to represent tumour
        :return:
        """
        self.patient = np.zeros([self.patient_size, self.patient_size])
        # add PTV
        PTV_ind = np.sqrt((self.X**2 + self.Y**2)) < self.PTV_radius
        self.patient[PTV_ind] = 1

    def visualize_patient(self):
        plt.figure()
        plt.imshow(self.patient)
        plt.show()


class Beam:
    def __init__(self,patient, angle=0):

        self.angle = angle
        assert angle in [0, 90, 180, 270]  # only support cardinal angles
        self.linear_attenuation = patient.linear_attenuation_coefficient
        self.patient = patient
        self.n_neamlets = 51  # make this larger than patient_size to ensure coverage!
        assert self.n_neamlets % 2 == 1
        self.width_at_iso = self.n_neamlets # this means we have exactly one beamlet per voxel at iso
        self.beamlet_weights = np.ones(self.n_neamlets)
        self._generate_coordinates()
        self._calculate_sensitivity_matrix()

    def update_beamlet_weights(self, new_weights):
        self.beamlet_weights = new_weights

    def _generate_coordinates(self):

        bounds = np.floor(self.n_neamlets / 2)
        self.x = np.linspace(-bounds, bounds, self.n_neamlets)

    def _calculate_sensitivity_matrix(self):
        """
        this matrix tells us the effect of each individual beamlet on each voxel of the Patient
            - the sensitivity matrix has one column per beamlet
            - each column contains the effect of that beamlets on every voxel in the patient

        Our dose calculation is going to be extremely simple:
        - each beamlet is completely parralel, e.g. no divergence through the patient
        - as the beamlet travels through the patient, the dose decays exponentially
        - the beam can only be from one of the four cardinal angles, because then we handle the beam angle just by rotating
            data!
        :return:
        """

        self.sensitivity_matrix = np.zeros([self.n_neamlets, self.patient.patient_size**2])
        depth_coords = np.linspace(0,self.patient.patient_size-1, self.patient.patient_size)

        for n_nbeamlet, beamlet_x in enumerate(self.x):
            _dose_matrix_temp = np.zeros([self.patient.patient_size, self.patient.patient_size])
            for i, patient_x in enumerate(self.patient.x):
                if beamlet_x == patient_x:
                    # then this beamlet intersects with the patient
                    dose_x = 1 * np.exp(-1 * self.linear_attenuation * depth_coords)
                    # this just defines an exponental decay, now we have to put it in the right place in the dose matrix
                    _dose_matrix_temp[:, i] = dose_x
                else:
                    '''
                    if the beamlet doesn't intersect with the patient, the sensitivity matrix is just 0
                    since we already defined it as zeros, we don't actually have to do anything
                    '''
                    pass

            '''
            - ok, at this point, we have the effect of one beamlet on every voxel in the patient
            - I'm going to handle the beam angle with a simple rotation operation - it's a pretty dodgy approach
            but it will work here
            '''
            rotated_angle = 0
            while rotated_angle < self.angle:
                _dose_matrix_temp = np.rot90(_dose_matrix_temp)
                rotated_angle = rotated_angle + 90
            # then flatten it and put it in the sensitivity matrix
            self.sensitivity_matrix[n_nbeamlet, :] = _dose_matrix_temp.flatten()


class DoseCalculater:
    """
    Takes one instance of Patient and N instances of Beam, and calculates the aggregate dose in Patient from all beams
    """

    def __init__(self, Patient, Beams=None):
        self.Patient = Patient
        self.Beams = Beams
        self.dose_array = np.zeros(self.Patient.patient.shape)

    def calculate_dose(self):

        for beam in self.Beams:
            for i, beamlet_sensitivity_array in enumerate(beam.sensitivity_matrix):
                beamlet_dose = beam.beamlet_weights[i] * beamlet_sensitivity_array
                self.dose_array = self.dose_array + np.reshape(beamlet_dose, self.dose_array.shape)

    def display_dose(self):
        plt.figure()
        plt.imshow(self.dose_array)

    def plot_DVH(self):
        pass


class LinearOptimizer:
    pass

if __name__ == '__main__':

    my_patient = Patient()
    beam_1 = Beam(my_patient, angle=0)
    beam_2 = Beam(my_patient, angle=90)
    beam_3 = Beam(my_patient, angle=180)
    beam_4 = Beam(my_patient, angle=270)

    dose = DoseCalculater(my_patient, [beam_1])
    dose.calculate_dose()
    dose.display_dose()