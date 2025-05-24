import os
import subprocess

class Updater:
    def __init__(self, repo_url, local_path):
        self.repo_url = repo_url
        self.local_path = local_path

    def check_for_updates(self):
        if os.path.exists(self.local_path):
            os.chdir(self.local_path)
            result = subprocess.run(['git', 'fetch'], capture_output=True, text=True)
            if result.returncode != 0:
                print("Error fetching updates:", result.stderr)
                return False
            result = subprocess.run(['git', 'status'], capture_output=True, text=True)
            if "Your branch is behind" in result.stdout:
                return True
        else:
            print("Local repository not found. Cloning...")
            self.clone_repository()
            return False
        return False

    def clone_repository(self):
        subprocess.run(['git', 'clone', self.repo_url, self.local_path])

    def update_repository(self):
        os.chdir(self.local_path)
        subprocess.run(['git', 'pull'])

    def run_update(self):
        if self.check_for_updates():
            print("Updates available. Updating...")
            self.update_repository()
            print("Update completed.")
        else:
            print("No updates available or local repository created.")

# Example usage:
# updater = Updater('https://github.com/your/repo.git', 'path/to/local/repo')
# updater.run_update()