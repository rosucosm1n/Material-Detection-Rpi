import torch
import torch.nn as nn
from torchvision import transforms
from PIL import Image

class MaterialCNN(nn.Module):
    def __init__(self):
        super(MaterialCNN, self).__init__()
        self.conv = nn.Sequential(
            nn.Conv2d(3, 16, 3, padding=1), nn.ReLU(), nn.MaxPool2d(2),
            nn.Conv2d(16, 32, 3, padding=1), nn.ReLU(), nn.MaxPool2d(2)
        )
        self.fc = nn.Sequential(
            nn.Flatten(),
            nn.Linear(32 * 16 * 16, 128),
            nn.ReLU(),
            nn.Linear(128, 3)
        )

    def forward(self, x):
        return self.fc(self.conv(x))

model = MaterialCNN()
model.load_state_dict(torch.load("model_cnn_materiale.pt", map_location=torch.device("cpu")))
model.eval()

transform = transforms.Compose([
    transforms.Resize((64, 64)),
    transforms.ToTensor(),
    transforms.Normalize([0.5], [0.5])
])
labels = ["carton", "plastic", "sticla"]

def prezice_material(imagine_path):
    try:
        image = Image.open(imagine_path).convert("RGB")
        input_tensor = transform(image).unsqueeze(0)
        with torch.no_grad():
            output = model(input_tensor)
            _, predicted = torch.max(output, 1)
        return labels[predicted.item()]
    except Exception as e:
        return "eroare"